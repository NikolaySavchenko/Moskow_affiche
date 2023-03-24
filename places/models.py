from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Описание точки')
    longitude = models.FloatField('Долгота:')
    latitude = models.FloatField('Широта:')

    def __str__(self):
        return self.title


class Images(models.Model):
    place = models.ForeignKey(Places, related_name='images',
                              on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    position = models.PositiveIntegerField('Позиция к показу', default=99,
                                           blank=True, null=True)

    def __str__(self):
        return self.place.title

    class Meta:
        ordering = ['position']
