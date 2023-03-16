from rest_framework import serializers
from .models import UserProfile

class ProcessSerializer(serializers.ModelSerializer):
    stripe_url = serializers.CharField()
    stripe_customer_id = serializers.CharField()
    coinbase_url = serializers.CharField()
    class Meta:
        model = UserProfile
        fields = ('subscribed', 'trial', 'stripe_url', 'stripe_customer_id', 'coinbase_url')

class SuccessSerializer(serializers.ModelSerializer):
    url = serializers.CharField()
    status = serializers.BooleanField()
    class Meta:
        model = UserProfile
        fields = ('subscribed', 'method', 'url', 'status')