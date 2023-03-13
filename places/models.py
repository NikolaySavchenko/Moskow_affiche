from django.db import models
from tinymce.models import HTMLField

class Places(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.CharField(max_length=500)
    description_long = HTMLField(max_length=10000)
    longitude = models.FloatField('Долгота:', max_length=20)
    latitude = models.FloatField('Широта:', max_length=20)

    def __str__(self):
        return self.title


class Images(models.Model):
    place = models.ForeignKey(Places, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    position = models.PositiveIntegerField('Позиция к показу', default=99,
                                           blank=True, null=True)

    class Meta:
        ordering = ['position']
