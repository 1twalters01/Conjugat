# Generated by Django 4.1.4 on 2023-01-17 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_paymentmethod'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='userprofile',
            new_name='subscriptio_user_id_19ea87_idx',
            old_name='subscriptio_user_id_97eb3b_idx',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='method_payment', to='subscription.paymentmethod'),
        ),
    ]
