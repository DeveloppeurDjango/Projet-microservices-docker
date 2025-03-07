# Generated by Django 5.0.4 on 2024-05-16 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppChefAgence', '0005_operateretraite_delete_operationretraite'),
    ]

    operations = [
        migrations.AddField(
            model_name='operateretraite',
            name='beneficiaire',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='operateretraite',
            name='nni',
            field=models.CharField(default='', max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Le NNI doit contenir exactement 10 chiffres.')]),
        ),
        migrations.AddField(
            model_name='operateretraite',
            name='ordre',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
