# Generated by Django 5.1.4 on 2024-12-10 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_verificationtoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationtoken',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='verification_tokens', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]