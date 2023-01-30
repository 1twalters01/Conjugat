from django.contrib import admin
from .models import Theme, TwoFactorAuth

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['user', 'theme']

@admin.register(TwoFactorAuth)
class TwoFactorAuthAdmin(admin.ModelAdmin):
    list_display = ['user', 'key', 'confirmed']