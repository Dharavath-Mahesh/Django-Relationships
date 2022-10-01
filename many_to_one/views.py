from django.shortcuts import render
from .models import Album, Song, AlbumSong
# Create your views here.
def manytoone(request):
    albums = Album.objects.all()
    songs = Song.objects.all()
    album_songs = AlbumSong.objects.all()

    context = {
        'albums': albums,
        'songs':songs,
        'album_songs': album_songs
    }

    return render(request, 'one-to-many.html', context)