from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import datetime
from subscription.models import UserProfile

# Unsubscribe users with expired subscriptions
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_active=True)
        for user in users:
            try:
                profile = UserProfile.objects.get(user=user)
            except:
                profile = None
            
            if profile:
                if profile.subscribed == True:
                    if profile.end_date > datetime.now().date():
                        profile.subscribed = False
                        profile.save()