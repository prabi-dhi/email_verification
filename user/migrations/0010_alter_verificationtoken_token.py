# Generated by Django 5.1.4 on 2024-12-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationtoken',
            name='token',
            field=models.CharField(editable=False, max_length=6, unique=True),
        ),
    ]
