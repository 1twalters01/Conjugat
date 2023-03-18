from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class LoginUsernameSerializer(serializers.ModelSerializer):
    confirmed = serializers.BooleanField()
    class Meta:
        model = User
        fields = ('username', 'confirmed')

class LoginPasswordSerializer(serializers.ModelSerializer):
    theme = serializers.CharField()
    class Meta:
        model = Token
        fields = ('key', 'theme')