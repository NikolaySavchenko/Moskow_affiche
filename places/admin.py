from django.contrib import admin
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from .secondary_tools import preview_image

from .models import Places, Images


class ImagesStackedInline(SortableStackedInline):
    model = Images
    readonly_fields = (preview_image,)
    fields = ('image', preview_image, 'position')


@admin.register(Places)
class SortablePlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImagesStackedInline]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    readonly_fields = (preview_image,)
