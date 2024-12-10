# Generated by Django 5.1.4 on 2024-12-10 11:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_verificationtoken_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationtoken',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verification_tokens', to=settings.AUTH_USER_MODEL),
        ),
    ]
