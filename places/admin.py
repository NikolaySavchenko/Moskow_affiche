from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from .secondary_tools import preview_image

from .models import Places, Images


class ImagesStackedInline(SortableStackedInline):
    model = Images
    readonly_fields = ['preview_image']

    def preview_image(self, picture):
        return format_html(
            mark_safe('<img src="{url}" height={height} />'),
            url=picture.image.url,
            height=200,
        )

    fields = ('image', 'preview_image', 'position')


@admin.register(Places)
class SortablePlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImagesStackedInline]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']

    def preview_image(self, picture):
        return format_html(
            mark_safe('<img src="{url}" height={height} />'),
            url=picture.image.url,
            height=200,
        )
