from django.conf import settings
from django.db import models
from verbs.models import RomanceMain
from nouns.models import RomanceNoun
from adjectives.models import RomanceAdjectives

class TestIdDigits(models.Model):
    digits = models.IntegerField(default=1)
    def __str__(self):
        return str(self.digits)

class Flags(models.Model):
    flag = models.CharField(max_length=20)
    def __str__(self):
        return self.flag

class DefaultTags(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flag = models.CharField(max_length=50)
    def __str__(self):
        return self.flag
    
class CustomTags(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flag = models.CharField(max_length=50)
    def __str__(self):
        return self.flag

class DefaultDifficulty(models.Model):
    difficulty = models.CharField(max_length=20)
    multiplier = models.FloatField()
    def __str__(self):
        return self.difficulty

class CustomDifficulty(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=20)
    multiplier = models.FloatField()
    def __str__(self):
        return self.difficulty

class VerbTestTime(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    test = models.ForeignKey(RomanceMain, on_delete=models.CASCADE, related_name='verb_timer')
    def __str__(self):
        return f'{self.test.conjugation.conjugation} {self.dateTime}'
    
class NounTestTime(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    test = models.ForeignKey(RomanceNoun, on_delete=models.CASCADE, related_name='noun_timer')
    def __str__(self):
        return f'{self.test.noun} {self.dateTime}'

class AdjectiveTestTime(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    test = models.ForeignKey(RomanceAdjectives, on_delete=models.CASCADE, related_name='noun_timer')
    def __str__(self):
        return f'{self.test.adjectives} {self.dateTime}'