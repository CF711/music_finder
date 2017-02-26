from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^artists/(?P<artist_id>[0-9]+)$', views.artist_view, name='artist'),
    url(r'^album/(?P<album_id>[0-9]+)$', views.album_view, name='album'),
    url(r'^song/(?P<song_id>[0-9]+)$', views.song_view, name='song'),
    #url(r'^artists/(?P<artist_name>[A-Za-z\s]+)$', views.artist_view, name='artist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)