# Generated by Django 4.1.6 on 2023-03-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_alter_places_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция к показу'),
        ),
    ]