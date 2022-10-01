from django.contrib import admin
from .models import Album, Song, AlbumSong
# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display= ['album_name']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name']


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ['singer', 'album', 'song']
