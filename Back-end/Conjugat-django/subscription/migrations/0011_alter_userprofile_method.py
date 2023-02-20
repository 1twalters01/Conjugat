# Generated by Django 4.1.4 on 2023-01-17 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0010_alter_userprofile_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='method',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='method_payment', to='subscription.paymentmethod'),
        ),
    ]