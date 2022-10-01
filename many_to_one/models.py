from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Album(models.Model): #An album can have many songs
    album_name = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name

class Song(models.Model): # song an have only one album
    song_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.song_name

class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.OneToOneField(Song, on_delete= models.CASCADE)
    singer = models.CharField(max_length=100)

    def __str__(self):
        return self.singer