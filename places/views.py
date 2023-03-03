from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import *


def index(request):
    places = Places.objects.all()

    context_final = {
        'places': {"type": 'FeatureCollection',
                   'features': []}
    }
    for place in places:
        place_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.title,
                "detailsUrl": reverse(place_content, args=str(place.id))
            }
        }

        context_final['places']['features'].append(place_geojson)

    return render(request, 'index.html', context=context_final)


def place_content(request, id):
    place = get_object_or_404(Places, id=id)
    images = Images.objects.filter(place_id=id).order_by('position')

    place_context = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }

    return JsonResponse(place_context,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
