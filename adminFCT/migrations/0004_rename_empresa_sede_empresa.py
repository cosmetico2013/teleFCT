# Generated by Django 4.1.2 on 2023-01-27 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminFCT', '0003_sede'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sede',
            old_name='Empresa',
            new_name='empresa',
        ),
    ]