# Generated by Django 4.1.4 on 2023-01-17 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_rename_subscriptio_user_id_97eb3b_idx_subscriptio_user_id_19ea87_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='method_payment', to='subscription.paymentmethod'),
        ),
    ]
