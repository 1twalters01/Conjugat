# Generated by Django 4.1.3 on 2023-04-12 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RomanceGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RomancePlurality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plural', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RomanceNoun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun', models.CharField(max_length=50)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noun_gender', to='nouns.romancegender')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noun_language', to='nouns.language')),
                ('plural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noun_plurality', to='nouns.romanceplurality')),
            ],
        ),
    ]
