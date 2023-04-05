from django.conf import settings
from django.db import models

class PaymentMethod(models.Model):
    method = models.CharField(max_length=20)
    def __str__(self):
        return self.method

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='method_payment', default=4)
    customer_id = models.CharField(max_length=500, blank=True, null=True)
    subscription_id = models.CharField(max_length=500, blank=True, null=True)
    subscribed = models.BooleanField(default=False)
    trial = models.BooleanField(default=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    class Meta:
        indexes = [
        models.Index(fields=['user', 'method', 'customer_id', 'subscription_id']),
        ]