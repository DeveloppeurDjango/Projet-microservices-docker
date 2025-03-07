# Generated by Django 5.0.4 on 2024-06-04 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppChefAgence', '0011_alter_listretraite_options_operateretraite_ordre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listretraite',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='operateretraite',
            options={'ordering': ['date_operation']},
        ),
        migrations.AddField(
            model_name='listretraite',
            name='ordre',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
