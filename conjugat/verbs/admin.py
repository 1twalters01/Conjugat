from django.contrib import admin
from .models import Language, RomanceBase, RomanceTense, RomanceSubject, RomanceAuxiliary, RomanceConjugation, RomanceMain, Progress

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language', 'id']

@admin.register(RomanceBase)
class RomanceBaseAdmin(admin.ModelAdmin):
    list_display = ['language', 'base', 'rank', 'id']
    list_filter = ['language']
    search_fields = ['language', 'base', 'rank']
    ordering = ['rank']

@admin.register(RomanceTense)
class RomanceTenseAdmin(admin.ModelAdmin):
    list_display = ['language', 'tense', 'id']
    list_filter = ['language']
    search_fields = ['language']

@admin.register(RomanceSubject)
class RomanceSubjectAdmin(admin.ModelAdmin):
    list_display = ['language', 'subject', 'id']
    list_filter = ['language']
    search_fields = ['language']

@admin.register(RomanceAuxiliary)
class RomanceAuxiliaryAdmin(admin.ModelAdmin):
    list_display = ['language', 'auxiliary', 'id']
    list_filter = ['language']
    search_fields = ['language']

@admin.register(RomanceConjugation)
class RomanceConjugationsAdmin(admin.ModelAdmin):
    list_display = ['base', 'conjugation', 'id']
    list_filter = ['base__language']
    search_fields = ['base__language', 'base__base', 'conjugation']

@admin.register(RomanceMain)
class RomanceMainAdmin(admin.ModelAdmin):
    list_display = ['rank', 'tense', 'subject', 'auxiliary', 'conjugation', 'id']
    list_filter = ['tense', 'tense__language', 'subject']
    search_fields = ['subject', 'auxiliary', 'conjugation', 'id']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'rank']
    list_filter = ['language']
    search_fields = ['user']