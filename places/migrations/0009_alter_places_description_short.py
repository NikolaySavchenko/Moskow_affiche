# Generated by Django 4.1.6 on 2023-03-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_places_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='description_short',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
    ]
