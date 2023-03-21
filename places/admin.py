from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableStackedInline
from adminsortable2.admin import SortableAdminBase

from .models import *


class ImagesStackedInline(SortableStackedInline):
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
class SortablePlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImagesStackedInline]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=200,
        )
        )
