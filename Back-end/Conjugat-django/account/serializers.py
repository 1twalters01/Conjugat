from base64 import urlsafe_b64decode
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from settings.models import TwoFactorAuth
from django.utils.encoding import force_str
from .tokens import account_activation_token, password_reset_token




class LoginUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmed = serializers.BooleanField(required=False)
    def validate_user(self, data):
        try:
            user = User.objects.get(username=data['username'])
        except:
            user = None
        if not user:
            try:
                user = User.objects.get(email=data['username'])
            except:
                user = None
            if not user:
                error = 'User was not found'
                return error, False
            
        active = user.is_active
        if active == False:
            error = 'User has not been activated'
            return error, False
        
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=user)
            confirmed = TwoFactor.confirmed
        except:
            TwoFactor = None
            confirmed = False
        response = {"username":user.username, "confirmed":confirmed}
        return response, True

class ActivateSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    def activate_user(self, data):        
        try:
            uid = urlsafe_b64decode(data['uidb64']+'=')
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if not user:
            error = 'user does not exist'
            return error, False
        
        if user.is_active:
            error = 'user has already been activated'
            return error, False
        
        token = data['token']
        if account_activation_token.check_token(user, token) != True:
            error = 'invalid token'
            return error, False
        
        user.is_active = True
        user.save()
        response = 'Successfully activated user'
        return response, True

class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()
    def activate_user(self, data):        
        try:
            uid = urlsafe_b64decode(data['uidb64']+'=')
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if not user:
            error = 'user does not exist'
            return error, False
        
        token = data['token']
        if password_reset_token.check_token(user, token) != True:
            error = 'invalid token'
            return error, False
        
        
        user.set_password(data['password'])
        user.save()
        response = 'Successfully changed password'
        return response, True




class LoginPasswordSerializer(serializers.ModelSerializer):
    theme = serializers.CharField()
    class Meta:
        model = Token
        fields = ('key', 'theme')


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    domain = serializers.CharField(read_only=True)