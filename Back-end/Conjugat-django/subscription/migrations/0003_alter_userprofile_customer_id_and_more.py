# Generated by Django 4.1.4 on 2023-01-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_alter_userprofile_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscription_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]