# Generated by Django 4.1.2 on 2023-01-31 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminFCT', '0012_rename_nombre_funcion_nomfun_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oferta',
            old_name='nombre',
            new_name='nomOfe',
        ),
    ]