# Generated by Django 4.1.3 on 2023-04-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testFunctionality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testiddigits',
            name='digits',
            field=models.IntegerField(default=1),
        ),
    ]
