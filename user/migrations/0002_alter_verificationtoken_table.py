# Generated by Django 5.1.4 on 2024-12-10 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='verificationtoken',
            table='tokens',
        ),
    ]
