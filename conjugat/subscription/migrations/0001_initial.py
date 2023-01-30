# Generated by Django 4.1.4 on 2023-01-03 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('subscription_id', models.CharField(blank=True, max_length=50, null=True)),
                ('subscribed', models.BooleanField(blank=True, default=False, null=True)),
                ('trial', models.BooleanField(blank=True, default=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
