from rest_framework import serializers
from .models import UserProfile

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('subscribed', 'trial')

class SuccessSerializer(serializers.ModelSerializer):
    charge = serializers.CharField()
    status = serializers.BooleanField()
    class Meta:
        model = UserProfile
        fields = ('subscribed', 'method', 'charge', 'status')