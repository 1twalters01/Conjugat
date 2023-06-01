from django.conf import settings
from django.db import models

# Theme
class Theme(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choices = (("Light", "Light"), ("Dark", "Dark"))
    theme = models.CharField(max_length=255, default='Light', choices=choices)
    def __str__(self):
        return self.theme

# Language
class Language(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choices = (("English", "English"), ("French", "French"), ("Italian", "Italian"), ("Portuguese", "Portuguese"), ("Spanish", "Spanish"))
    language = models.CharField(max_length=255, default='English', choices=choices)
    def __str__(self):
        return self.language

# Typography
class Typeface(models.Model):
    typeface = models.CharField(max_length=20)
    def __str__(self):
        return self.typeface

class FontDB(models.Model):
    font = models.CharField(max_length=100)
    typeface = models.ForeignKey(Typeface, on_delete=models.CASCADE, related_name='fontDB_typeface')
    def __str__(self):
        return self.font

class Font(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headerFont = models.ForeignKey(FontDB, on_delete=models.CASCADE, related_name='header_font', null=True)
    bodyFont = models.ForeignKey(FontDB, on_delete=models.CASCADE, related_name='body_font', null=True)

# 2FA
class TwoFactorAuth(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=500)
    confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.confirmed