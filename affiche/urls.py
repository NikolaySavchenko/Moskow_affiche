from django.contrib import admin
from django.urls import path
from places import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('places/<int:id>', views.places),
    path('', views.index),
    ] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
