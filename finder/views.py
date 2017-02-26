from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Artist, Album, Song

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'artist_list'

    def get_queryset(self):
        return Artist.objects.all()[:5]


def artist_view(request, artist_id):
    artist = Artist.objects.filter(id=artist_id).first()
    albums = Album.objects.filter(album_artist=artist_id)
    context = {
    	'artist': artist,
    	'albums': albums
    }

    return render(request, 'finder/artist.html', context)

def album_view(request, album_id):
    album = Album.objects.filter(id=album_id).first()
    songs = Song.objects.filter(song_album=album_id)
    artist = album.getArtist()
    context = {
    	'album': album,
    	'songs': songs,
    	'artist': artist
    }

    return render(request, 'finder/album.html', context)

def song_view(request, song_id):
    song = Song.objects.filter(id=song_id).first()
    album = song.getAlbum()
    artist = song.getArtist()
    context = {
    	'album': album,
    	'song': song,
    	'artist': artist
    }

    return render(request, 'finder/song.html', context)