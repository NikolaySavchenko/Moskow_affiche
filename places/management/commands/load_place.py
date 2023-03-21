from urllib import parse, request

import requests
from django.core.management.base import BaseCommand

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

        Places.objects.get_or_create(
            title=response.json()['title'],
            description_short=response.json()['description_short'],
            description_long=response.json()['description_long'],
            longitude=response.json()['coordinates']['lng'],
            latitude=response.json()['coordinates']['lat'],
        )
        title = response.json()['title']
        place = Places.objects.get(title=title)

        for num, img in enumerate(response.json()['imgs']):
            pict = request.urlopen(img).read()
            out = open(f'media/media/{title}_{num}.jpg', "wb")
            out.write(pict)
            out.close

            Images.objects.get_or_create(
                place=place,
                image=f'media/{title}_{num}.jpg',
                position=num
            )
