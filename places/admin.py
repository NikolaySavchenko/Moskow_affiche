from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ImagesInline(admin.TabularInline):
    model = Images
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=200,
        )
        )

    fields = ('image', 'preview_image', 'position')


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=200,
        )
        )
