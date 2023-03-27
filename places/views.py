from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import Places, Images


def index(request):
    places = Places.objects.all()
    features = []

    for place in places:
        point = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse(place_content,
                                      kwargs={'id': place.id})
            }
        }
        features.append(point)

    final_context = {
        'places': {
            'type': 'FeatureCollection',
            'features': features
        }
    }

    return render(request, 'index.html', context=final_context)


def place_content(request, id):
    place = get_object_or_404(Places, id=id)
    images = place.images.all()

    place_context = {
        'title': place.title,
        'imgs': [image.image.url for image in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        }
    }

    return JsonResponse(
        place_context,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
