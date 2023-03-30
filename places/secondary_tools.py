from django.utils.html import format_html


def preview_image(picture):
    return format_html(
        '<img src="{url}" height={height} />',
        url=picture.image.url,
        height=200,
    )
