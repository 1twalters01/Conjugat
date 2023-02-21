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
from rest_framework.authtoken.models import Token

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
            'method': 'POST',
            'body': {'body': ""},
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

def is_two_factor_active(user):
    try:
        TwoFactor = TwoFactorAuth.objects.get(user=user)
        confirmed = TwoFactor.confirmed
    except:
        TwoFactor = None
        confirmed = False
    return confirmed

from.serializers import LoginUsernameSerializer

@api_view(["POST"])
@permission_classes([AllowAny])
def loginUsernameView(request):
    username = request.data.get("username")
    print(request.data)
    if username is None:
        return Response({'error': 'No username was entered'},
                        status=status.HTTP_400_BAD_REQUEST)

    user, activeCheck = does_username_exist(username)
    if not user:
        return Response({'error': 'Username is not recognised'},
                        status=status.HTTP_400_BAD_REQUEST)
    if activeCheck != True:
        return Response({'error': 'User is not activated'},
                        status=status.HTTP_400_BAD_REQUEST)

    user.confirmed = is_two_factor_active(user.id)
    serializer = LoginUsernameSerializer(user)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)




'''
Need to make the remember_me functionality
    app - never resign in unless extended period of not being signed in
    pc - once a month and every day respectively
Need to have functionality to have each sign in platform have its own token
'''
def login_procedure(request, user, remember_me):
    if not remember_me:
        request.session.set_expiry(0)
    login(request, user)

@api_view(["POST"])
@permission_classes([AllowAny])
def loginPasswordView(request):
    username = request.data.get("username")
    uid = request.data.get("id")
    password = request.data.get("password")
    totp = request.data.get("totp")
    confirmed = request.data.get("confirmed")
    remember_me = request.data.get("remember_me")
    print(username, uid, password, totp,confirmed)
    if not uid:
        return Response({'error': 'No username provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        uid = int(uid)
    except:
        uid = None
    if isinstance(uid, int) == False:
        print('User id must be an integer')
        return Response({'error': 'User id must be an integer'},
                        status=status.HTTP_400_BAD_REQUEST)
    if not password:
        print('No password provided')
        return Response({'error': 'No password provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    if not confirmed:
        print('No totp status provided')
        return Response({'error': 'No totp status provided'},
                        status=status.HTTP_400_BAD_REQUEST)

    if confirmed == 'True' or confirmed == 'true':
        confirmed = True
    elif confirmed == 'False' or confirmed == 'false':
        confirmed = False
    
    if isinstance(confirmed, bool) == False:
        print('totp status must be a boolean')
        return Response({'error': 'totp status must be a boolean'},
                        status=status.HTTP_400_BAD_REQUEST)

    
    user = authenticate(username=username, password=password)
    if not user:
        print('The username and/or password is incorrect')
        return Response({'error': 'The username and/or password is incorrect'},
                        status=status.HTTP_404_NOT_FOUND)
    
    if confirmed:
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=uid)
            key = decrypt(TwoFactor.key).encode('ascii')
            totpCheck = generate_totp(key)
        except:
            print('uid is not found')
            return Response({'error': 'uid is not found'},
                        status=status.HTTP_404_NOT_FOUND)
    else:
        totpCheck = None
        totp = None
    if totpCheck != totp:
        print('The totp is incorrect')
        return Response({'error': 'The totp is incorrect'},
                        status=status.HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)






@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logoutView(request):
    token = request.headers.get("Authorization").split('Token ')[1]
    try:
        token = Token.objects.get(key=token)
    except (AttributeError, ObjectDoesNotExist):
        token = None
    if not token:
        return Response({'error': 'invalid authentication token'},
                        status=status.HTTP_400_BAD_REQUEST)
    token.delete()
    return Response({"success": "Successfully logged out."},
                    status=status.HTTP_200_OK)


# I am using django to send the email. I could use mailchimp instead.
@api_view(["POST"])
@permission_classes([AllowAny])
def registerView(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    password2 = request.data.get("password2")
    domain = request.data.get("domain")
    
    if username is None or email is None or password is None or password2 is None:
        print('Please fill in all form fields')
        return Response({'error': 'Please fill in all form fields'},
                        status=status.HTTP_400_BAD_REQUEST)
    if password != password2:
        print('Passwords must match')
        return Response({'error': 'Passwords must match'},
                        status=status.HTTP_400_BAD_REQUEST)      
    try:
        usernameTest = User.objects.get(username=username)
        emailTest = User.objects.get(email=email)
    except:
        usernameTest = None
        emailTest = None
    if usernameTest is not None or emailTest is not None:
        print('User already exists')
        return Response({'error': 'User already exists'},
                        status=status.HTTP_400_BAD_REQUEST)
                        
    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.is_active = False
    user.save()

    try:
        subject = 'Conjugat activation email'
        message = render_to_string('registration/activate_email.html', {
            'user': user,
            'domain': domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        recipient = email
        email = EmailMessage(subject, message, to=[recipient])
        email.send()
    except:
        print('Unable to send to email address')
        return Response({'error': 'Unable to send to email address'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"success": "Successfully created user. Activate with link in email."},
                status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def activateView(request):
    uidb64 = request.data.get("uidb64")
    token = request.data.get("token")
    print(uidb64, token)
    print(get_current_site(request).domain)
    if uidb64 is None or token is None:
        return Response({'error': 'Invalid url type'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if not user:
        return Response({'error': 'user does not exist'},
                        status=status.HTTP_400_BAD_REQUEST)
    if user.is_active:
        return Response({'error': 'user has already been activated'},
                        status=status.HTTP_400_BAD_REQUEST)
    if account_activation_token.check_token(user, token) != True:
        return Response({'error': 'invalid token'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    user.is_active = True
    user.save()
    return Response({"success": "Successfully activated user"},
            status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def passwordResetView(request):
    email = request.data.get("email")
    domain = request.data.get("domain")
    print(email, domain)
    if not email:
        return Response({'error': 'No email provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(email=email)
    except:
        user = None
    if user == None:
        return Response({'error': 'Email has no associated account or hasn\'t been activated'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        subject = 'Conjugat password reset'
        message = render_to_string('registration/password_reset_email.html', {
            'user': user,
            'domain': domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':password_reset_token.make_token(user),
        })
        recipient = email
        email = EmailMessage(subject, message, to=[recipient])
        email.send()
    except:
        print('Unable to send to email address')
        return Response({'error': 'Unable to send to email address'},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({"success": "Password reset email has been sent"},
                status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def passwordResetConfirmView(request):
    uidb64 = request.data.get("uidb64")
    token = request.data.get("token")
    password = request.data.get("password")
    password2 = request.data.get("password2")
    print(uidb64, token)

    if uidb64 is None or token is None:
        return Response({'error': 'Invalid url type'},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if not user:
        return Response({'error': 'user does not exist'},
                        status=status.HTTP_400_BAD_REQUEST)
    if password_reset_token.check_token(user, token) != True:
        print('invalid token')
        return Response({'error': 'invalid token'},
                        status=status.HTTP_400_BAD_REQUEST)
    if password != password2:
        return Response({'error': 'Passwords must match'},
                        status=status.HTTP_400_BAD_REQUEST)

    if user and password_reset_token.check_token(user, token):
        user.set_password(password)
        user.save()
    return Response({"success": "Successfully changed password"},
            status=status.HTTP_200_OK)