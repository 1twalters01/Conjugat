from django.contrib import admin
from .models import UserProfile, PaymentMethod

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['method', 'pk']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'method', 'subscribed', 'trial', 'customer_id', 'subscription_id', 'start_date', 'end_date']
    raw_id_fields = ['user']