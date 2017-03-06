from django.contrib import admin

from .models import Song, Album, Artist, SameArtistVote, DifferentArtistVote

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(SameArtistVote)
admin.site.register(DifferentArtistVote)