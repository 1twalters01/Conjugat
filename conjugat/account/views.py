from .forms import UsernameForm, totpForm, passwordForm, UserRegistrationForm, PasswordResetForm, SetPasswordForm
from .tokens import account_activation_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from settings.models import TwoFactorAuth
from settings.totp import generate_totp
from subscription.encryption import decrypt


from rest_framework import status
from rest_framework.authtoken.models import Token   
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist

@api_view(["GET"])
@permission_classes([AllowAny])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/login/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Authenticates the user'
        },
        {
            'Endpoint': '/logout/',
            'method': 'GET',
            'body': None,
            'description': 'Logs out the user'
        },
        {
            'Endpoint': '/register/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Registers a new, unactivated user'
        },
    ]
    return Response(routes)


@api_view(["POST"])
@permission_classes([AllowAny])
def loginView(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logoutView(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    logout(request)
    return Response({"success": "Successfully logged out."},
                    status=status.HTTP_200_OK)

@api_view(["PUT"])
@permission_classes([AllowAny])
def registerView(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    password2 = request.data.get("password2")

    if username is None or email is None or password is None or password2 is None:
        return Response({'error': 'Please fill in all form fields'},
                        status=status.HTTP_400_BAD_REQUEST)
    if password != password2:
        return Response({'error': 'Passwords must match'},
                        status=status.HTTP_400_BAD_REQUEST)      
    try:
        usernameTest = User.objects.get(username=username)
        emailTest = User.objects.get(email=email)
    except:
        usernameTest = None
        emailTest = None
    if usernameTest is not None or emailTest is not None:
        return Response({'error': 'User already exists'},
                        status=status.HTTP_400_BAD_REQUEST)
                        
    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.is_active = False
    user.save()

    subject = 'Conjugat activation email'
    current_site = get_current_site(request)
    message = render_to_string('registration/active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    })
    recipient = email
    email = EmailMessage(subject, message, to=[recipient])
    email.send()

    return Response({"success": "Successfully created user. Activate with link in email."},
                status=status.HTTP_200_OK)





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
    kwargs = {'navbar':False}
    success_url = reverse_lazy("password_reset_done")

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
        return render(request, 'registration/register.html', {'user_form':user_form, 'navbar':False})


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
        return render(request, 'registration/register_done.html', {'new_user':user})
        # return HttpResponse('Activation link is invalid!')