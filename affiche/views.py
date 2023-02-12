from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # template = loader.get_template('index.html')
    # context = {}
    # rendered_page = template.render(context, request)
    # return HttpResponse(rendered_page)
    # Все строки выше заменяются шорткастом render
    return render(request, 'index.html')