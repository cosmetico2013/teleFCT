# Generated by Django 4.1.2 on 2023-03-13 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminFCT', '0002_rename_distritos_distrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='cpSed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminFCT.distrito'),
        ),
    ]
