from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Count
from smart_selects.db_fields import ChainedManyToManyField
from embed_video.fields import EmbedVideoField

# Create your models here.

class Song(models.Model):
	title=models.CharField(max_length=255)
	# Need to do validation on the client side
	other_artist_linked_songs = models.ManyToManyField('DifferentArtistVote', blank=True)
	same_artist_linked_songs = models.ManyToManyField('SameArtistVote', blank=True)
	artist = models.ForeignKey('Artist')
	song_album = models.ForeignKey('Album')
	video = EmbedVideoField(blank=True)

	def __str__(self):
		return self.title

	def getLinkedCount(self):
		return Count(same_artist_linked_song) + Count(other_artist_linked_songs)

	def getAlbum(self):
		return self.song_album

	def getArtist(self):
		return self.artist

	def toString(self):
		return self.title

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

class SameArtistVote(models.Model):
	votes = models.IntegerField(default=0)
	artist_song = models.ForeignKey('Song', related_name="artist_song")
	related_song = models.ForeignKey('Song', related_name="related_song")

	def __str__(self):
		song1 = "'" + self.artist_song.toString() + "'"
		song2 = "'" + self.related_song.toString() + "'"
		return song1 + " to " + song2

class DifferentArtistVote(models.Model):
	votes = models.IntegerField(default=0)
	artist_one_song = models.ForeignKey('Song', related_name="artist_one_song")
	artist_two_song = models.ForeignKey('Song', related_name="artist_two_song")

	def __str__(self):
		song1 = "'" + self.artist_one_song.toString() + "'"
		song2 = "'" + self.artist_two_song.toString() + "'"
		return song1 + " to " + song2