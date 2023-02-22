from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=500)
    description_long = models.CharField(max_length=10000)
    longitude = models.FloatField('Долгота:', max_length=20)
    latitude = models.FloatField('Широта:', max_length=20)

    def __str__(self):
        return self.title
