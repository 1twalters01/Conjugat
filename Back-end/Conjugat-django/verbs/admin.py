from django.contrib import admin
from .models import Language, RomanceBase, RomanceTense, RomanceSubject, RomanceAuxiliary, RomanceConjugation, RomanceMain, RomanceTestResult, RomanceTestResult_by_user_and_date, RomanceTestResult_by_user_and_language, Progress

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

@admin.register(RomanceTestResult)
class RomanceTestResultAdmin(admin.ModelAdmin):
    list_display = ['testID', 'user', 'language', 'rank', 'answers', 'status', 'StartDateTime', 'EndDateTime']

@admin.register(RomanceTestResult_by_user_and_date)
class RomanceTestResult_by_user_and_dateAdmin(admin.ModelAdmin):
    list_display = ['EndDateTime', 'testID', 'user']

@admin.register(RomanceTestResult_by_user_and_language)
class RomanceTestResult_by_user_and_languageAdmin(admin.ModelAdmin):
    list_display = ['testID', 'user', 'language']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'rank']
    list_filter = ['language']
    search_fields = ['user']