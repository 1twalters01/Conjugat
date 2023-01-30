from .forms import CloseAccountForm, ChangePasswordForm, ChangeEmailForm, ChangeUsernameForm, ThemesForm, TOTPForm, ResetAccountForm
from .models import Theme, TwoFactorAuth
from .totp import create_key_of_length, generate_totp, generate_QR_string_and_code
from coinbase_commerce.client import Client
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView#
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from subscription.encryption import decrypt, encrypt
from subscription.models import UserProfile
from subscription.paypal import suspend_sub, activate_sub
import stripe
from verbs.models import Progress


def payment_method(method):
    if method == 'Stripe':
        return 1
    elif method == 'Paypal':
        return 2
    elif method == 'Coinbase':
        return 3

from subscription.paypal import cancel_sub
@login_required
def close_account(request):
    if request.method == 'POST':
        form = CloseAccountForm(request.POST, initial='test')
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(username=request.user)
            if user.check_password(cd['password']) == True:
                # See if user has premium account and if so delete it
                try:
                    premium = UserProfile.objects.get(user=request.user)
                except:
                    premium = None
                if premium:
                    if premium.method_id == payment_method('Stripe'):
                        # stop subscription
                        if premium.subscription_id:
                            customer = decrypt(premium.customer_id)
                            subscription = decrypt(premium.subscription_id)
                            stripe.api_key = settings.STRIPE_SECRET_KEY
                            print(customer)
                            stripe.Customer.delete(customer)
                    if premium.method_id == payment_method('Paypal'):
                        cancel_sub(decrypt(premium.subscription_id))
                    premium.delete()
                # Delete the user
                # user.delete()
                return redirect('landing')
    form = CloseAccountForm()
    context = {'form':form}
    return render(request, 'settings/close_account.html', context)


class change_password(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy("change_password_done")
    template_name = "settings/change_password_form.html"


class change_password_done(PasswordChangeDoneView):
    title = "settings/change_password_done.html"


@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, initial='test')
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(username=request.user)
            if user.check_password(cd['password']) == True:
                try:
                    check = User.objects.get(email=cd['email'])
                except:
                    check = None
                if check == None:
                    user.email = cd['email']
                    user.save()
                    return redirect('settings:change_email_done')
                else:
                    HttpResponse("Email is already in use")
            else:
                form = ChangeEmailForm()
                context = {'form':form}
                return render(request, 'settings/change_email_form.html', context)
    else:
        form = ChangeEmailForm()
        context = {'form':form}
        return render(request, 'settings/change_email_form.html', context)


@login_required
def change_email_done(request):
    context = {}
    return render(request, 'settings/change_email_done.html', context)


@login_required
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST, initial='test')
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(username=request.user)
            if user.check_password(cd['password']) == True:
                try:
                    check = User.objects.get(username=cd['username'])
                except:
                    check = None
                if check == None:
                    user.username = cd['username']
                    user.save()
                    # Check if there is a premium account associated with this
                    try:
                        userProfile = UserProfile.objects.get(user=request.user)
                    except:
                        userProfile = None
                    if userProfile:
                        userProfile.user = cd['username']
                        userProfile.save()
                    return redirect('change_username_done')
                else:
                    HttpResponse("Email is already in use")
            else:
                form = ChangeUsernameForm()
                context = {'form':form}
                return render(request, 'settings/change_username_form.html', context)
    else:
        form = ChangeUsernameForm()
        context = {'form':form}
        return render(request, 'settings/change_username_form.html', context)


@login_required
def change_username_done(request):
    context = {}
    return render(request, 'settings/change_username_done.html', context)


@login_required
def themes(request):
    if request.method == 'POST':
        form = ThemesForm(request.POST, initial='test')
        theme = Theme.objects.get(user=request.user)
        if form.is_valid():
            selected = form.cleaned_data.get("theme")
            theme.theme = selected
            theme.save()
            return redirect('settings:themes')
    else:
        form = ThemesForm()
        context = {'form': form}
        return render(request, 'settings/themes.html', context)


@login_required
def premium(request):
    try:
        user = UserProfile.objects.get(user=request.user)
    except:
        user = None
    if user:
        if user.subscribed == True:
            if user.method_id == payment_method('Stripe'):
                premium = user.subscribed
                context = {'premium': user.subscribed, 'method': 'Stripe'}
                if request.method == 'POST':
                    # This is the URL to which the customer will be redirected after they are
                    # done managing their billing with the portal.
                    return_url = request.build_absolute_uri(reverse('settings:premium'))

                    portalSession = stripe.billing_portal.Session.create(
                        customer = decrypt(user.customer_id),
                        return_url=return_url,
                    )
                    return redirect(portalSession.url, code=303)
                else:
                    return render(request, 'settings/premium.html', context)
            elif user.method_id == payment_method('Paypal'):
                premium = user.subscribed
                context = {'premium': user.subscribed, 'method': 'Paypal'}
                if request.method == 'POST':
                    sub_id = decrypt(user.subscription_id)
                    if request.POST.get('Stop'):
                        suspend_sub(sub_id)
                        return redirect('settings:premium')

                    elif request.POST.get('Re-start'):
                        activate_sub(sub_id)
                        return redirect('settings:premium')
                else:
                    return render(request, 'settings/premium.html', context)
            elif user.method_if == payment_method('Coinbase'):
                charge_id = decrypt(user.subscription_id)
                client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
                charge = client.charge.retrieve(charge_id)
                context = {'premium':user.subscribed, 'method': 'Coinbase', 'charge':charge}

    premium = None
    context = {'premium': premium}
    return render(request, 'settings/premium.html', context)



@login_required
def two_factor_auth(request):
    try:
        TwoFactor = TwoFactorAuth.objects.get(user=request.user)
        confirmed = TwoFactor.confirmed
    except:
        TwoFactor = None
        confirmed = None
    length_of_OTP = 6
    step_in_seconds = 30
    
    if request.method == 'POST':
        form = TOTPForm(request.POST)

        if not TwoFactor or TwoFactor.confirmed == False:
            key = decrypt(TwoFactor.key).encode('ascii')
            totp = generate_totp(key, length_of_OTP, step_in_seconds)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.get(username=request.user)
                if user.check_password(cd['password']) and cd['totp'] == int(totp):
                    TwoFactor.confirmed = True
                    TwoFactor.save()
                    return redirect('settings:two_factor_auth')
                else:
                    return redirect('settings:two_factor_auth')
                    
        elif TwoFactor.confirmed == True:
            key = decrypt(TwoFactor.key).encode('ascii')
            totp = generate_totp(key, length_of_OTP, step_in_seconds)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.get(username=request.user)
                if user.check_password(cd['password']) and cd['totp'] == int(totp):
                    TwoFactor.confirmed = False
                    TwoFactor.save()
                    return redirect('settings:two_factor_auth')
                else:
                    return redirect('settings:two_factor_auth')

    else:
        form = TOTPForm()
        if not TwoFactor or TwoFactor.confirmed == False:
            key = create_key_of_length(20)
            if not TwoFactor:
                TwoFactor = TwoFactorAuth.objects.create(user=request.user)
            TwoFactor.key = encrypt(key.decode('ascii'))
            TwoFactor.save()
            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email, length_of_OTP, step_in_seconds)
            context = {'qr_string':qr_string, 'form':form, 'confirmed':confirmed}

        else:
            key = decrypt(TwoFactor.key).encode('ascii')

            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email, length_of_OTP, step_in_seconds)
            context = {'qr_string':qr_string, 'form':form, 'confirmed':confirmed}
        return render(request,'settings/qrcode.html', context)


@login_required
def reset_account(request):
    if request.method == 'POST':
        form = ResetAccountForm(request.POST, initial='test')
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(username=request.user)
            if user.check_password(cd['password']) == True:
                print(cd['language'], type(cd['language']))
                if cd['language'] == 'All':
                    try:
                        account = Progress.objects.filter(user=request.user)
                    except:
                        account = None
                else:
                    try:
                        account = Progress.objects.get(user=request.user, language=cd['language'])
                    except:
                        account = None
                if account:
                    account.delete()
                return redirect('settings:reset_account')
    form = ResetAccountForm()
    context = {'form':form}
    return render(request, 'settings/reset_account.html', context)