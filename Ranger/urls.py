from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from RangerApp.views import create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RangerApp.urls')),
    path('', create_view, name='create_view')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

