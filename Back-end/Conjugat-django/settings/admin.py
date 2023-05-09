from django.contrib import admin
from .models import Theme, Language, TwoFactorAuth

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['user', 'theme']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user', 'language']

@admin.register(TwoFactorAuth)
class TwoFactorAuthAdmin(admin.ModelAdmin):
    list_display = ['user', 'key', 'confirmed']