# Generated by Django 4.1.4 on 2023-04-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_alter_subscriptionstatus_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='newslettersubscriber',
            index=models.Index(fields=['user', 'status'], name='newsletter__user_id_81f0b9_idx'),
        ),
    ]
