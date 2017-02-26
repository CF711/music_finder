from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Count
from smart_selects.db_fields import ChainedManyToManyField

# Create your models here.

class Song(models.Model):
	title=models.CharField(max_length=255)
	# Need to do validation on the client side
	other_artist_linked_songs = models.ManyToManyField('self', blank=True)
	same_artist_linked_songs = ChainedManyToManyField(
		'self', 
		chained_field = 'artist',
		chained_model_field = 'artist',
		)
	artist = models.ForeignKey('Artist')
	song_album = models.ForeignKey('Album')

	def __str__(self):
		return self.title

	def getLinkedCount(self):
		return Count(same_artist_linked_song) + Count(other_artist_linked_songs)

	def getAlbum(self):
		return self.song_album

	def getArtist(self):
		return self.artist

class Album(models.Model):
	songs = ChainedManyToManyField(
		Song, 
		chained_field = "album_artist",
		chained_model_field = "artist",
		blank=True
		)
	title = models.CharField(max_length=255)
	year = models.IntegerField()
	album_artist = models.ForeignKey('Artist')
	album_art = models.ImageField(upload_to='albums', blank=True)

	def __str__(self):
		return self.title

	def getArtist(self):
		return self.album_artist

	def getLinkedCount(self):
		count = 0
		for song in songs:
			count += song.getLinkedCount()
		return count

class Artist(models.Model):
	name = models.CharField(max_length=255)
	albums = models.ManyToManyField(Album, blank=True)

	def __str__(self):
		return self.name

	def getAlbums(self):
		return self.albums