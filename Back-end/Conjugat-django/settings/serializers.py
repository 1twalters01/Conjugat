from django.contrib.auth.models import User
from rest_framework import serializers

class ChangeUserSerializer(serializers.ModelSerializer):
    confirmed = serializers.BooleanField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password')