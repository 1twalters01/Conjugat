from .forms import UsernameForm, totpForm, passwordForm, UserRegistrationForm, PasswordResetForm, SetPasswordForm
from .tokens import account_activation_token, password_reset_token
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
            'description': 'Check if the user has totp activated'
        },
        {
            'Endpoint': '/login/password/',
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
        {
            'Endpoint': '/activate/<uidb64>/<token>/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Activate a newly registered user'
        },
        {
            'Endpoint': '/password-reset/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Send a password reset email'
        },
        {
            'Endpoint': '/password-reset/<uidb64>/<token>/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Reset a password for a user'
        },
    ]
    return Response(routes)


def does_username_exist(username):
    try:
        user = User.objects.get(username=username)
        active = user.is_active
    except:
        user = None
        active = None
    if not user:
        try:
            user = User.objects.get(email=username)
            active = user.is_active
        except:
            user = None
        active = None
    return user, active

def is_two_factor_active(username):
    try:
        TwoFactor = TwoFactorAuth.objects.get(user=username)
        confirmed = TwoFactor.confirmed
    except:
        TwoFactor = None
        confirmed = None
    return confirmed

@api_view(["POST"])
@permission_classes([AllowAny])
def loginView(request):
    username = request.data.get("username")
    if username is None:
        return Response({'error': 'No username was entered'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    usernameCheck, activeCheck = does_username_exist(username)
    if not usernameCheck:
        return Response({'error': 'Username is not recognised'},
                        status=status.HTTP_400_BAD_REQUEST)
    if activeCheck != True:
        return Response({'error': 'User is not activated'},
                        status=status.HTTP_400_BAD_REQUEST)

    confirmed = is_two_factor_active(username)
    return Response({'username': username, 'confirmed': confirmed},
                    status=status.HTTP_200_OK)







'''
Need to make the remember_me functionality 
'''
def login_procedure(request, user, remember_me):
    if not remember_me:
        request.session.set_expiry(0)
    login(request, user)

@api_view(["POST"])
@permission_classes([AllowAny])
def loginPasswordView(request):
    username = request.data.get("username")
    password = request.data.get("password")
    totp = request.data.get("totp")
    confirmed = request.data.get("confirmed")
    remember_me = request.data.get("remember_me")

    if confirmed:
        TwoFactor = TwoFactorAuth.objects.get(user=username[1])
        key = decrypt(TwoFactor.key).encode('ascii')
        totpCheck = generate_totp(key)
    else:
        totpCheck = None
        totp = None
    if totpCheck != totp:
        return Response({'error': 'The totp is incorrect'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'The password is incorrect'},
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


# I am using django to send the email. I could use mailchimp instead.
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
    message = render_to_string('registration/activate_email.html', {
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


@api_view(["POST"])
@permission_classes([AllowAny])
def activateView(request):
    uidb64 = request.data.get("uidb64")
    token = request.data.get("token")
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({"success": "Successfully activated user"},
                status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Activation link is invalid'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def passwordResetView(request):
    email = request.data.get("email")
    try:
        user = User.objects.get(email)
    except:
        pass
    if user is None:
        return Response({'error': 'Email has no associated account'},
                        status=status.HTTP_400_BAD_REQUEST)
    if user.is_active == False:
        return Response({'error': 'User has not been activated'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    subject = 'Conjugat password reset'
    current_site = get_current_site(request)
    message = render_to_string('registration/password_reset_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':password_reset_token.make_token(user),
    })
    recipient = email
    email = EmailMessage(subject, message, to=[recipient])
    email.send()

    return Response({"success": "Password reset email has been sent"},
                status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def passwordResetConfirmView(request):
    uidb64 = request.data.get("uidb64")
    token = request.data.get("token")
    password = request.data.get("password")
    password2 = request.data.get("password2")
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if password != password2:
        return Response({'error': 'Passwords must match'},
                        status=status.HTTP_400_BAD_REQUEST)

    if user and account_activation_token.check_token(user, token):
        user.set_password(password)
        user.save()
