from base64 import urlsafe_b64decode
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from settings.models import Theme, TwoFactorAuth
from settings.totp import generate_totp
from subscription.encryption import decrypt
from subscription.models import UserProfile
from .tokens import account_activation_token, password_reset_token
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token


class LoginUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmed = serializers.BooleanField(required=False)
    def obtain_user(self, username):
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

    def is_2FA_active(self, user):
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=user)
            confirmed = TwoFactor.confirmed
        except:
            TwoFactor = None
            confirmed = False
        return confirmed

    def validate_user(self, user):
        if not user:
            error = 'User was not found'
            return error, False
        
        if user.is_active == False:
            error = 'User has not been activated'
            return error, False
        return True, True

    def check_username(self, data):
        username = data['username']
        user = self.obtain_user(username)

        validated_user = self.validate_user(user)
        if validated_user[1] == False:
            return validated_user[0], validated_user[1]

        confirmed = self.is_2FA_active(user)
        response = {"username":user.username, "confirmed":confirmed}
        return response, True

class LoginPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    totp = serializers.CharField(required=False, allow_blank=True)
    remember_me = serializers.BooleanField()
    
    def validate_user(self, user):
        if not user:
            error = 'The username and/or password is incorrect'
            return error, False, status.HTTP_401_UNAUTHORIZED
        return True, True

    def validate_2FA(self, user, totp):
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=user.id)
            key = decrypt(TwoFactor.key).encode('ascii')
            totpCheck = generate_totp(key)
        except:
            TwoFactor = None
            totpCheck = ''

        if totpCheck != totp:
            error = 'The totp is incorrect'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True

    def obtain_token(self, remember_me, user):
        if remember_me == True:
            # Token expiration date for 1 week
            token, _ = Token.objects.get_or_create(user=user)
        elif remember_me == False:
            #token expiration date for 1 day
            token, _ = Token.objects.get_or_create(user=user)
        return token

    def login_user(self, data):
        username = data['username']
        password = data['password']
        totp = data['totp']
        remember_me = data['remember_me']
  
        user = authenticate(username=username, password=password)
        validated_user = self.validate_user(user)
        if validated_user[1] == False:
            return validated_user[0], validated_user[1], validated_user[2]

        validated_2FA = self.validate_2FA(user, totp)
        if validated_2FA[1] == False:
            return validated_2FA[0], validated_2FA[1], validated_2FA[2]
        
        token = self.obtain_token(remember_me, user)
        theme = Theme.objects.get_or_create(user=user)[0]
        response = {'key':token.key, 'theme':theme.theme}
        return response, True
'''
Need to make the remember_me functionality
    app - never resign in unless extended period of not being signed in
    pc - once a month and every day respectively
Need to have functionality to have each sign in platform have its own token
'''

''' Register '''
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()
    domain = serializers.CharField()
    def obtain_user_via_username(self, username):
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        return user
    
    def obtain_user_via_email(self, email):
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        return user
    
    def create_email(self, user, domain, email):
        subject = 'Conjugat activation email'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        message = render_to_string('activate_email.html', {
            'user': user,
            'domain': domain,
            'uid':uid,
            'token':account_activation_token.make_token(user),
        })
        recipient = email
        email = EmailMessage(subject, message, to=[recipient])
        return email

    def register_user(self, data):
        username = data['username']
        email = data['email']
        password = data['password']
        domain = data['domain']
        
        if self.obtain_user_via_username(username):
            error = 'Username already exists'
            return error, False, status.HTTP_409_CONFLICT
        
        if self.obtain_user_via_email(email):
            error = 'Email already exists'
            return error, False, status.HTTP_409_CONFLICT
                       
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.is_active = False
        user.save()

        try:
            email = self.create_email(user, domain, email).send()
            emailed = True
        except:
            emailed = False

        if emailed == False:
            user.delete()
            error = 'Unable to send to email address'
            return error, False, status.HTTP_424_FAILED_DEPENDENCY
        
        subscriber = UserProfile.objects.create(user=user, method_id=4)
        subscriber.save()
        response = "Successfully created user. Activate with link in email."
        return response, True

class ActivateSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    def obtain_user(self, uidb64):
        try:
            uid = urlsafe_b64decode(uidb64+'=')
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user
    
    def validate_user(self, user):
        if not user:
            error = 'user does not exist'
            return error, False
        
        if user.is_active:
            error = 'user has already been activated'
            return error, False
        return True, True
    
    def validate_activation_token(self, user, token):
        if account_activation_token.check_token(user, token) != True:
            error = 'invalid token'
            return error, False
        return True, True

    def activate_user(self, data):
        uidb64 = data['uidb64']
        token = data['token']
        user = self.obtain_user(uidb64)

        validated_user = self.validate_user(user)
        if validated_user[1] == False:
            return validated_user[0], validated_user[1]

        validated_token = self.validate_activation_token(user, token)
        if validated_token[1] == False:
            return validated_token[0], validated_token[1]

        user.is_active = True
        user.save()
        response = 'Successfully activated user'
        return response, True


''' Password reset '''
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    domain = serializers.CharField(read_only=True)
    def get_user_from_email(self, email):
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        return user
    
    def create_email(self, user, domain, email):
        subject = 'Conjugat activation email'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        message = render_to_string('password_reset_email.html', {
            'user': user,
            'domain': domain,
            'uid':uid,
            'token':account_activation_token.make_token(user),
        })
        recipient = email
        email = EmailMessage(subject, message, to=[recipient])
        return email
    
    def send_password_reset_email(self, data):
        email = data['email']
        domain = data['domain']
        user = self.get_user_from_email(email)
        if user == None:
            error = 'Email has no associated account or hasn\'t been activated'
            return error, False, status.HTTP_424_FAILED_DEPENDENCY
        try:
            email = self.create_email(user, domain, email).send()
            emailed = True
        except:
            emailed = False

        if emailed == False:
            error = 'Unable to send to email address'
            return error, False, status.HTTP_424_FAILED_DEPENDENCY
        
        response = "Password reset email has been sent"
        return response, True

class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()
    def obtain_user(self, uidb64):
        try:
            uid = urlsafe_b64decode(uidb64+'=')
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user

    def validate_user(self, user):
        if not user:
            error = 'user does not exist'
            return error, False
        return True, True

    def validate_password_reset_token(self, user, token):
        if password_reset_token.check_token(user, token) != True:
            error = 'invalid token'
            return error, False
        return True, True

    def save_password(self, user, password):
        user.set_password(password)
        user.save()

    def activate_user(self, data):
        uidb64 = data['uidb64']
        token = data['token']
        password = data['password']

        user = self.obtain_user(uidb64)
        validated_user = self.validate_user(user)
        if validated_user[1] == False:
            return validated_user[0], validated_user[1]
        
        validated_token = self.validate_password_reset_token(user, token)
        if validated_token[1] == False:
            return validated_token[0], validated_token[1]

        self.save_password(user, password)
        response = 'Successfully changed password'
        return response, True