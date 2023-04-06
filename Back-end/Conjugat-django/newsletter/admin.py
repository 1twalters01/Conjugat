from django.contrib import admin
from .models import NewsletterSubscriber, SubscriptionStatus

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'pk']

@admin.register(SubscriptionStatus)
class SubscriptionStatus(admin.ModelAdmin):
    list_display = ['status', 'id']