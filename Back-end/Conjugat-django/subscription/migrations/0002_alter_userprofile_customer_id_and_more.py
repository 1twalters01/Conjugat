# Generated by Django 4.1.4 on 2023-01-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscription_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
