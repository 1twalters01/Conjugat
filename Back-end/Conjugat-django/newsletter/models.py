from django.conf import settings
from django.db import models

class SubscriptionStatus(models.Model):
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.method

class NewsletterSubscribers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.ForeignKey(SubscriptionStatus, on_delete=models.CASCADE, related_name='subscription_status')