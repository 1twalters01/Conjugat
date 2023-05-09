from django.conf import settings
from django.db import models

class Theme(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(max_length=255, default='Light')

class Language(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    options = (("English", "English"), ("French", "French"), ("Italian", "Italian"), ("Portuguese", "Portuguese"), ("Spanish", "Spanish"))
    language = models.CharField(max_length=255, default='English')

class TwoFactorAuth(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=500)
    confirmed = models.BooleanField(default=False)