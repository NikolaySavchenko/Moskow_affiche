# Generated by Django 4.1.6 on 2023-03-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_places_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='latitude',
            field=models.FloatField(verbose_name='Широта:'),
        ),
        migrations.AlterField(
            model_name='places',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота:'),
        ),
    ]
