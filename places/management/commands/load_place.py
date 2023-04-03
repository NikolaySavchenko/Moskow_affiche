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
            nargs=1,
            help='Enter the URL of the json with a description of the point'
        )

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        url_parse = parse.urlsplit(*url)
        url_rezult = f'{url_parse.scheme}://{url_parse.netloc}{url_parse.path}{url_parse.query}{url_parse.fragment}'

        response = requests.get(url_rezult)
        response.raise_for_status()
        place_specification = response.json()
        same_places = Places.objects.filter(
            longitude=place_specification['coordinates']['lng'],
            latitude=place_specification['coordinates']['lat'],
        )
        if same_places:
            print(f"Данная точка: {place_specification['title']}, уже отмечена на карте")
            exit()

        title = place_specification['title']

        place, __ = Places.objects.update_or_create(
            title=title,
            defaults={
                'title': title,
                'description_short': place_specification.get('description_short', ''),
                'description_long': place_specification.get('description_long', ''),
                'longitude': place_specification['coordinates']['lng'],
                'latitude': place_specification['coordinates']['lat'],
            }
        )

        for num, img in enumerate(place_specification.get('imgs', [])):
            pict = request.urlopen(img)
            Images.objects.get_or_create(
                place=place,
                image=ContentFile(pict.read(), name=f'{place.id}_{num}.jpg'),
                position=num
            )
