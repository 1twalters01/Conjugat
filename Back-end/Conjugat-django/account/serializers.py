from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from settings.models import TwoFactorAuth

class ActivateSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()

class LoginUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmed = serializers.BooleanField(required=False)
    def valid_user(self, data):
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






class LoginPasswordSerializer(serializers.ModelSerializer):
    theme = serializers.CharField()
    class Meta:
        model = Token
        fields = ('key', 'theme')


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    domain = serializers.CharField(read_only=True)

# class PasswordResetConfirmationSerializer(serializers.Serializer):
#     uidb64 = serializers.CharField(read_only=True)
#     token = serializers(read_only=True)
#     password = serializers(read_only=True)
#     password2 = serializers(read_only=True)