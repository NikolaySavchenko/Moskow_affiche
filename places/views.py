from django.shortcuts import render
import json
from .models import *


def index(request):
    places = Places.objects.all()

    context_final = {
        'places': {"type": 'FeatureCollection',
                   'features': []}
    }
    for place in places:
        place_context = {
            "title": place.title,
            "imgs": [],  # place.images,
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude,
            }
        }

        place_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.title,
                "detailsUrl": json.dumps(place_context)
            }
        }

        context_final['places']['features'].append(place_geojson)

    return render(request, 'index.html', context=context_final)
