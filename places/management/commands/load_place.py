from urllib import parse, request

import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Places, Images


class Command(BaseCommand):
    help = 'Add a new place in database'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            nargs='*',
            help='Enter the URL of the json with a description of the point'
        )

    def handle(self, *args, **kwargs):
        url = kwargs['url'][0]
        url_parse = parse.urlsplit(url)
        url_rez = f'{url_parse.scheme}://{url_parse.netloc}{url_parse.path}'

        response = requests.get(url_rez)
        response.raise_for_status()
        place = Places.objects.filter(
            longitude=response.json()['coordinates']['lng'],
            latitude=response.json()['coordinates']['lat'],
        )
        if place:
            print(f"Данная точка: {response.json()['title']}, уже отмечена на карте")
            exit()

        title = response.json()['title']

        Places.objects.get_or_create(
            title=title,
            description_short=response.json()['description_short'],
            description_long=response.json()['description_long'],
            longitude=response.json()['coordinates']['lng'],
            latitude=response.json()['coordinates']['lat'],
        )

        place = Places.objects.get(title=title)

        for num, img in enumerate(response.json()['imgs']):
            pict = request.urlopen(img)
            Images.objects.get_or_create(
                place=place,
                image=ContentFile(pict.read(), name=f'{place.id}_{num}.jpg'),
                position=num
            )
