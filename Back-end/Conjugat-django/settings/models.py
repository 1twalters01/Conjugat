from django.conf import settings
from django.db import models

class Theme(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choices = (("Light", "Light"), ("Dark", "Dark"))
    theme = models.CharField(max_length=255, default='Light', choices=choices)

class Language(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choices = (("English", "English"), ("French", "French"), ("Italian", "Italian"), ("Portuguese", "Portuguese"), ("Spanish", "Spanish"))
    language = models.CharField(max_length=255, default='English', choices=choices)

class Font(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choices = (("Light", "Light"), ("Dark", "Dark"))
    font = models.CharField(max_length=255, default='Light', choices=choices)

class TwoFactorAuth(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=500)
    confirmed = models.BooleanField(default=False)