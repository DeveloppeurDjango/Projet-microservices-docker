# Generated by Django 5.0.4 on 2024-06-04 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppChefAgence', '0016_listretraite_ordre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listretraite',
            name='ordre',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
