from django.utils.html import format_html
from django.utils.safestring import mark_safe


def preview_image(self, picture):
    return format_html(
        mark_safe('<img src="{url}" height={height} />'),
        url=picture.image.url,
        height=200,
    )