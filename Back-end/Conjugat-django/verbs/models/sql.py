# SQL DB models are put here
from django.db import models


# Language list
class Language(models.Model):
    language = models.CharField(max_length=30)
    def __str__(self):
        return self.language


# Model functionality for the base groups
class RomanceGroup(models.Model):
    group = models.CharField(max_length=10, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='group_language')
    class Meta:
        unique_together = (('group', 'language'),)
    def __str__(self):
        return self.group


class RomanceEnding(models.Model):
    ending = models.CharField()
    group = models.ForeignKey(RomanceGroup, on_delete=models.CASCADE, related_name='ending_group')
    class Meta:
        unique_together = (('ending', 'group'),)
    def __str__(self):
        return self.ending


class RomanceModel(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='model_language')
    model = models.CharField(max_length=50)
    ending = models.ForeignKey(RomanceEnding, on_delete=models.CASCADE, related_name='model_group')
    class Meta:
        unique_together = (('model', 'ending'),)
    def __str__(self):
        return self.model


# Main models
class RomanceTense(models.Model):
    tense = models.CharField(max_length=80) 
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='tense_lanugage')
    class Meta:
        unique_together = (('tense','language'),)
        indexes = [
            models.Index(fields=['tense']),
        ]
    def __str__(self):
        return self.tense


class RomanceBase(models.Model):
    base = models.CharField(max_length=50)
    rank = models.PositiveIntegerField()
    model = models.ForeignKey(RomanceModel, on_delete=models.CASCADE, related_name='base_model', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_base') # Remove?
    class Meta:
        unique_together = (('language','base'), ('language', 'rank'),)
        indexes = [
            models.Index(fields=['base']),
        ]
    def __str__(self):
        return self.base


class RomanceSubject(models.Model):
    subject = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='subject_language')
    class Meta:
        unique_together = (('subject','language'),)
        indexes = [
            models.Index(fields=['subject']),
        ]
    def __str__(self):
        return self.subject


class RomanceAuxiliary(models.Model):
    auxiliary = models.CharField(max_length=50, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='auxiliary_language')
    class Meta:
        unique_together = (('auxiliary','language'),)
        indexes = [
            models.Index(fields=['auxiliary']),
        ]
        verbose_name_plural = 'Romance auxiliaries'
    def __str__(self):
        return self.auxiliary


class RomanceConjugation(models.Model):
    conjugation = models.CharField(max_length=50)
    base = models.ForeignKey(RomanceBase, on_delete=models.CASCADE, related_name='conjugation_base')
    class Meta:
        unique_together = (('base','conjugation'),)
        indexes = [
        models.Index(fields=['conjugation']),
        ]
    def __str__(self):
        return self.conjugation


# Final model
class RomanceMain(models.Model):
    rank = models.PositiveIntegerField()
    tense = models.ForeignKey(RomanceTense, on_delete=models.CASCADE, related_name='main_tense')
    subject = models.ForeignKey(RomanceSubject, on_delete=models.CASCADE, related_name='main_subject')
    auxiliary = models.ForeignKey(RomanceAuxiliary, on_delete=models.CASCADE, related_name='main_auxiliary')
    conjugation = models.ForeignKey(RomanceConjugation, on_delete=models.CASCADE, related_name='main_conjugation')
    class Meta:
        unique_together = (('subject','auxiliary', 'conjugation'),)
        indexes = [
            models.Index(fields=['auxiliary']),
        ]
        verbose_name_plural = 'Romance main'
    def __str__(self):
        return f'{self.subject.language} {self.rank}'

