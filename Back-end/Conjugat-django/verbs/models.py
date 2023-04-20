from django.conf import settings
from django.db import models

import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class Language(models.Model):
    language = models.CharField(max_length=30)
    def __str__(self):
        return self.language


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


class RomanceBase(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_base')
    base = models.CharField(max_length=50)
    rank = models.PositiveIntegerField()
    class Meta:
        unique_together = (('language','base'), ('language', 'rank'),)
        indexes = [
        models.Index(fields=['base']),
        ]
    def __str__(self):
        return self.base


class RomanceGroup(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_group')
    group = models.CharField(max_length=10)
    class Meta:
        unique_together = (('language', 'group'),)
    def __str__(self):
        return self.group


class RomanceModel(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_model')
    group = models.ForeignKey(RomanceGroup, on_delete=models.CASCADE, related_name='group_model')
    model = models.CharField(max_length=50)
    class Meta:
        unique_together = (('language', 'model'),)
    def __str__(self):
        return self.model


class RomanceRhyme(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_rhyme')
    base = models.ForeignKey(RomanceBase, on_delete=models.CASCADE, related_name='bases_rhyme_base')
    rhymes = models.ForeignKey(RomanceBase, on_delete=models.CASCADE, related_name='bases_rhyme')
    class Meta:
        unique_together = (('language', 'base', 'rhymes'),)
        indexes = [
        models.Index(fields=['rhymes']),
        ]
    def __str__(self):
        return self.rhymes


class RomanceHalfRhyme(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_half_rhyme')
    base = models.ForeignKey(RomanceBase, on_delete=models.CASCADE, related_name='bases_half_rhyme_base')
    half_rhymes = models.ForeignKey(RomanceBase, on_delete=models.CASCADE, related_name='bases_half_rhyme')
    class Meta:
        unique_together = (('language', 'base', 'half_rhymes'),)
        indexes = [
        models.Index(fields=['half_rhymes']),
        ]
    def __str__(self):
        return self.half_rhymes


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
    conjugation = models.CharField(max_length=50)
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


class RomanceTestResult(DjangoCassandraModel):
    testID = columns.UUID(default=uuid.uuid4(), primary_key=True)
    user = columns.Integer()
    StartDateTime = columns.DateTime()
    EndDateTime = columns.DateTime()
    languages = columns.List(value_type=columns.Text())
    pks = columns.List(value_type=columns.Integer())
    tenses = columns.List(value_type=columns.Text())
    bases = columns.List(value_type=columns.Text())
    subjects = columns.List(value_type=columns.Text())
    auxiliaries = columns.List(value_type=columns.Text())
    conjugations = columns.List(value_type=columns.Text())
    status = columns.List(value_type=columns.Boolean())
    ranks = columns.List(value_type=columns.Integer())
    answers = columns.List(value_type=columns.Text())
    flags = columns.List(value_type=columns.Text())

class RomanceTestResult_by_user_and_language(DjangoCassandraModel):
    language = columns.Text(primary_key=True)
    testID = columns.UUID(default=uuid.uuid4(), primary_key=True)
    user = columns.Integer()
    class Meta:
        get_pk_field='language'

class RomanceTestResult_by_user_and_date(DjangoCassandraModel):
    user = columns.Integer(primary_key=True)
    EndDateTime = columns.DateTime(primary_key=True)
    testID = columns.UUID(default=uuid.uuid4())    
    class Meta:
        get_pk_field='user'






class Progress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_progress')
    rank = models.ForeignKey(RomanceMain, on_delete=models.CASCADE, related_name='rank_progress', default='5')