from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from itertools import chain

from .models import Artist, Album, Song, SameArtistVote, DifferentArtistVote

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
    print(song)
    print(song.getAlbum())
    print(song.getArtist())
    album = song.getAlbum()
    artist = song.getArtist()
    same_artist_related = getTopLinkedSong(list(chain(SameArtistVote.objects.filter(artist_song=song_id), SameArtistVote.objects.filter(related_song=song_id))), song_id)
    other_artist_related = getTopLinkedSong(list(chain(DifferentArtistVote.objects.filter(artist_one_song=song_id), DifferentArtistVote.objects.filter(artist_two_song=song_id))), song_id)
    context = {
    	'album': album,
    	'song': song,
    	'artist': artist,
        'same_artist_related': same_artist_related,
        'other_artist_related': other_artist_related
    }

    return render(request, 'finder/song.html', context)

def getTopLinkedSong(queryList, song_id):
    topSong = None
    for x in queryList:
        if topSong == None:
            topSong = x
        elif x.votes > topSong.votes:
            topSong = x
    if hasattr(topSong, 'artist_song'):
        return getTopArtistLinkedSong(topSong, song_id)
    elif hasattr(topSong, 'artist_one_song'):
        return getTopOtherLinkedSong(topSong, song_id)
    else:
        return None

def getTopArtistLinkedSong(songLink, song_id):
    if (int(songLink.artist_song.id) == int(song_id)):
        return songLink.related_song
    else:
        return songLink.artist_song

def getTopOtherLinkedSong(songLink, song_id):
    if (int(songLink.artist_one_song.id) == int(song_id)):
        return songLink.artist_two_song
    else:
        return songLink.artist_one_song