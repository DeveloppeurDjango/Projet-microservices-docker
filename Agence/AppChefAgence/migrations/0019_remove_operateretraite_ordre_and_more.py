# Generated by Django 5.0.4 on 2024-06-07 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppChefAgence', '0018_rename_ordre_listretraite_ordre_enregistrement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operateretraite',
            name='ordre',
        ),
        migrations.AddField(
            model_name='operateretraite',
            name='ordre_enregistrement',
            field=models.IntegerField(default=0),
        ),
    ]
