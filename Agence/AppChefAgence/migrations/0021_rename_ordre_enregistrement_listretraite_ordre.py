# Generated by Django 5.0.4 on 2024-06-08 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppChefAgence', '0020_remove_operateretraite_ordre_enregistrement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listretraite',
            old_name='ordre_enregistrement',
            new_name='ordre',
        ),
    ]
