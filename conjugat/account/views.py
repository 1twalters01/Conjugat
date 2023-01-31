from .forms import UsernameForm, totpForm, passwordForm, UserRegistrationForm, PasswordResetForm, SetPasswordForm
from .tokens import account_activation_token
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from settings.models import TwoFactorAuth
from settings.totp import generate_totp
from subscription.encryption import decrypt


def reset_username(request):
    request.session['username'] = None
    request.session['confirmed'] = None
    return None, None

def does_username_exist(username):
    try:
        user = User.objects.get(username=username)
    except:
        user = None
    if not user:
        try:
            user = User.objects.get(email=username)
        except:
            user = None
    return user

def is_two_factor_active(username):
    try:
        TwoFactor = TwoFactorAuth.objects.get(user=username)
        confirmed = TwoFactor.confirmed
    except:
        TwoFactor = None
        confirmed = None
    return confirmed


def get_totp_or_password_form(totp_enabled, request=None):
    if request:
        if totp_enabled:
            form = totpForm(request.POST, initial='test')
        else:
            form = passwordForm(request.POST, initial='test')
        return form

    if totp_enabled:
        form = totpForm()
    else:
        form = passwordForm()
    return form


def login_procedure(request, user, remember_me):
    if not remember_me:
        request.session.set_expiry(0)
    login(request, user)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        username = request.session.get('username', None)
        confirmed = request.session.get('confirmed', None)

        if request.method == 'POST':
            if request.POST.get('new-username'):
                username, confirmed = reset_username(request)
                return redirect('login')

            if not username:
                form = UsernameForm(request.POST, initial='test')
                if form.is_valid() != True:
                    return HttpResponse('invalid form')

                clean_data = form.cleaned_data
                username = does_username_exist(clean_data['username'])
                if not username:
                    return HttpResponse('username or email not found')

                confirmed = is_two_factor_active(username)
                request.session['username'] = [username.username, username.id]
                request.session['confirmed'] = confirmed
                form = totpForm()
                context = {'form':form, 'username':username, 'confirmed':confirmed, 'navbar':False}
                return redirect('home')

            else:
                form = get_totp_or_password_form(confirmed, request)
                if form.is_valid() == False:
                    return HttpResponse('invalid form')

                clean_data = form.cleaned_data
                user = authenticate(request, username=username[0], password=clean_data['password'])

                if user == None:
                    return HttpResponse('Incorrect password')
                if user.is_active != True:
                    return HttpResponse('Disabled account')

                if confirmed:
                    TwoFactor = TwoFactorAuth.objects.get(user=username[1])
                    key = decrypt(TwoFactor.key).encode('ascii')
                    totp = generate_totp(key)
                else:
                    clean_data['totp'] = None
                    totp = None

                if clean_data['totp'] != totp:
                    return HttpResponse('wrong totp')

                login_procedure(request, user, clean_data['remember_me'])
                username, confirmed = reset_username(request)
                return redirect('home')

        else:
            if username:
                form = get_totp_or_password_form(confirmed)
                context = {'form':form, 'username':username, 'confirmed':confirmed, 'navbar':False}
                return render(request, 'registration/login_password.html', context)
            else:
                form = UsernameForm()
                context = {'form':form, 'navbar':False}
                return render(request, 'registration/login.html', context)


class NewPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm

class NewPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm


# I am using django to send the email. I could use mailchimp instead.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =='POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.is_active = False
                user.save()
                current_site = get_current_site(request)

                subject = 'Conjugat activation email'
                message = render_to_string('registration/active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                recipient = user_form.cleaned_data.get('email')
                email = EmailMessage(subject, message, to=[recipient])
                email.send()
                return render(request, 'registration/register_verify.html', {'new_user':user})
        else:
            user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'user_form':user_form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/register_done.html', {'new_user':user})
    else:
        return HttpResponse('Activation link is invalid!')