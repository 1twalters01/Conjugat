from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from.serializers import LoginUsernameSerializer, LoginPasswordSerializer

from subscription.encryption import decrypt
from settings.models import TwoFactorAuth
from settings.totp import generate_totp
from .tokens import account_activation_token, password_reset_token


''' Routes '''
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


''' Login '''
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

@api_view(["POST"])
@permission_classes([AllowAny])
def loginUsernameView(request):
    username = request.data.get("username")

    if username is None:
        error = 'No username was entered'
        return Response({'error': error},
                        status=status.HTTP_404_NOT_FOUND)

    user, active = does_username_exist(username)
    if not user:
        error = 'Username is not recognised'
        return Response({'error': error},
                        status=status.HTTP_401_UNAUTHORIZED)
    if active == False:
        error = 'User is not activated'
        return Response({'error': error},
                        status=status.HTTP_401_UNAUTHORIZED)

    user.confirmed = is_two_factor_active(user.id)
    serializer = LoginUsernameSerializer(user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)




'''
Need to make the remember_me functionality
    app - never resign in unless extended period of not being signed in
    pc - once a month and every day respectively
Need to have functionality to have each sign in platform have its own token
'''
from settings.models import Theme
@api_view(["POST"])
@permission_classes([AllowAny])
def loginPasswordView(request):
    username = request.data.get("username")
    password = request.data.get("password")
    totp = request.data.get("totp")
    remember_me = request.data.get("remember_me")

    if not password:
        error = 'No password provided'
        print(error)
        return Response({'error': error},
                        status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    if not user:
        error = 'The username and/or password is incorrect'
        print(error)
        return Response({'error': error},
                        status=status.HTTP_404_NOT_FOUND)
    
    try:
        TwoFactor = TwoFactorAuth.objects.get(user=user.id)
        key = decrypt(TwoFactor.key).encode('ascii')
        totpCheck = generate_totp(key)
    except:
        TwoFactor = None
        totpCheck = ''
    print(totpCheck, totp)
    if totpCheck != totp:
        error = 'The totp is incorrect'
        print(error)
        return Response({'error': error},
                    status=status.HTTP_400_BAD_REQUEST)
    
    if remember_me == True:
        # Token expiration date for 1 week
        token, _ = Token.objects.get_or_create(user=user)
    elif remember_me == False:
        #token expiration date for 1 day
        token, _ = Token.objects.get_or_create(user=user)

    theme = Theme.objects.get_or_create(user=user)[0]
    token.theme = theme.theme
    serializer = LoginPasswordSerializer(token)
    return Response(data=serializer.data,
                    status=status.HTTP_200_OK)




from django.contrib.auth import logout
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logoutView(request):
    request.user.auth_token.delete()
    logout(request)
    success = "User has been successfully logged out"
    return Response({"success": success},
                    status=status.HTTP_204_NO_CONTENT)


from subscription.models import UserProfile
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
        error = 'Please fill in all form fields'
        print(error)
        return Response({'error': error},
                        status=status.HTTP_400_BAD_REQUEST)
    print(password, password2)
    if password != password2:
        error = 'Passwords must match'
        print(error)
        return Response({'error': error},
                        status=status.HTTP_400_BAD_REQUEST)      
    
    try:
        usernameTest = User.objects.get(username=username)
    except:
        usernameTest = None
    try:
        emailTest = User.objects.get(email=email)
    except:
        emailTest = None

    if usernameTest is not None :
        error = 'User already exists'
        print(error)
        return Response({'error': error},
                        status=status.HTTP_400_BAD_REQUEST)
    if emailTest is not None:
        error = 'Email already exists'
        print(error)
        return Response({'error': error},
                        status=status.HTTP_400_BAD_REQUEST)
                        
    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.is_active = False

    try:
        print(domain, email)
        subject = 'Conjugat activation email'
        message = render_to_string('activate_email.html', {
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
    
    user.save()
    subscriber = UserProfile.objects.create(user=user, method_id=4)
    subscriber.save()
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
        message = render_to_string('password_reset_email.html', {
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