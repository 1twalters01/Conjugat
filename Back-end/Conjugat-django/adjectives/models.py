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
    
class RomanceAdjectives(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='adjectives_language')
    gender = models.ForeignKey(RomanceGender, on_delete=models.CASCADE, related_name='adjectives_gender')
    plural = models.ForeignKey(RomancePlurality, on_delete=models.CASCADE, related_name='adjectives_plurality')
    adjectives = models.CharField(max_length=50)
    def __str__(self):
        return self.adjectives