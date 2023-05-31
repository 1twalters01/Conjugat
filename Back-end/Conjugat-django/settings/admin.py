from django.contrib import admin
from .models import Theme, TwoFactorAuth, Language, Typeface, FontDB, Font

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['user', 'theme']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user', 'language']

@admin.register(Typeface)
class TypefaceAdmin(admin.ModelAdmin):
    list_display = ['typeface']

@admin.register(FontDB)
class FontDBAdmin(admin.ModelAdmin):
    list_display = ['font', 'typeface']

@admin.register(Font)
class FontAdmin(admin.ModelAdmin):
    list_display = ['user', 'headerFont', 'bodyFont']

@admin.register(TwoFactorAuth)
class TwoFactorAuthAdmin(admin.ModelAdmin):
    list_display = ['user', 'key', 'confirmed']