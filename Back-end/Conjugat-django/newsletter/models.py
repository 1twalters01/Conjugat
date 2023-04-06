from django.conf import settings
from django.db import models

class SubscriptionStatus(models.Model):
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.status
    class Meta:
        verbose_name_plural = 'Subscription statuses'

class NewsletterSubscriber(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.ForeignKey(SubscriptionStatus, on_delete=models.CASCADE, related_name='subscription_status', default=2)
    class Meta:
        indexes = [
        models.Index(fields=['user', 'status']),
        ]