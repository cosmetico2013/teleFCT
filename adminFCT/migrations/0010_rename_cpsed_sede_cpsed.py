# Generated by Django 4.1.2 on 2023-02-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminFCT', '0009_alter_alumno_fnac_alter_contrato_fincon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sede',
            old_name='cpsed',
            new_name='cpSed',
        ),
    ]