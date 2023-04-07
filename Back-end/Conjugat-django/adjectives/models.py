from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=30)
    def __str__(self):
        return self.language
    
class RomanceGender(models.Model):
    gender = models.CharField(max_length=20)
    def __str__(self):
        return self.gender

class RomancePlurality(models.Model):
    plural = models.BooleanField()
    def __str__(self):
        return self.plural