# Generated by Django 4.1.2 on 2023-01-31 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminFCT', '0010_rename_nombre_tool_nomtoo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisito',
            old_name='nombre',
            new_name='nomReq',
        ),
    ]