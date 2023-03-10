from django.conf import settings
from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=30)
    def __str__(self):
        return self.language


class RomanceBase(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_base')
    base = models.CharField(max_length=20)
    rank = models.PositiveIntegerField()
    class Meta:
        unique_together = (('language','base'), ('language', 'rank'),)
        indexes = [
        models.Index(fields=['base']),
        ]
    def __str__(self):
        return self.base


class RomanceTense(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_tense')
    tense = models.CharField(max_length=80)
    class Meta:
        unique_together = (('tense','language'),)
        indexes = [
        models.Index(fields=['tense']),
        ]
    def __str__(self):
        return self.tense


class RomanceSubject(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_subject')
    subject = models.CharField(max_length=20)
    class Meta:
        unique_together = (('subject','language'),)
        indexes = [
        models.Index(fields=['subject']),
        ]
    def __str__(self):
        return self.subject


class RomanceAuxiliary(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_auxiliary')
    auxiliary = models.CharField(max_length=50, blank=True)
    class Meta:
        unique_together = (('auxiliary','language'),)
        indexes = [
        models.Index(fields=['auxiliary']),
        ]
        verbose_name_plural = 'Romance auxiliaries'
    def __str__(self):
        return self.auxiliary


class RomanceConjugation(models.Model):
    base = models.ForeignKey(RomanceBase, on_delete=models.CASCADE, related_name='bases')
    conjugation = models.CharField(max_length=40)
    class Meta:
        unique_together = (('base','conjugation'),)
        indexes = [
        models.Index(fields=['conjugation']),
        ]
    def __str__(self):
        return self.conjugation


class RomanceMain(models.Model):
    rank = models.PositiveIntegerField()
    tense = models.ForeignKey(RomanceTense, on_delete=models.CASCADE, related_name='tense_main')
    subject = models.ForeignKey(RomanceSubject, on_delete=models.CASCADE, related_name='subject_main')
    auxiliary = models.ForeignKey(RomanceAuxiliary, on_delete=models.CASCADE, related_name='auxiliary_main')
    conjugation = models.ForeignKey(RomanceConjugation, on_delete=models.CASCADE, related_name='conjugation_main')
    class Meta:
        unique_together = (('subject','auxiliary', 'conjugation'),)
        indexes = [
            models.Index(fields=['auxiliary']),
        ]
        verbose_name_plural = 'Romance main'
    def __str__(self):
        return f'{self.subject.language} {self.rank}'


class Progress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_progress')
    rank = models.ForeignKey(RomanceMain, on_delete=models.CASCADE, related_name='rank_progress', default='5')