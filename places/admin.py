from django.contrib import admin

from .models import *


class ImagesInline(admin.TabularInline):
    model = Images


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


admin.site.register(Images)
