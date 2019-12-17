from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Album, Track
from rest_framework import generics
from .serializers import ArtistSerializer
from Music.forms import AlbumForm, TrackForm
# Create your views here.



def Artist_list(request):
    art_list = User.objects.all()
    return render(request,'Music/home.html',{'art_list':art_list} )

def album_list(request,pk):
    artist = get_object_or_404(User,pk=pk)
    #alb = artist.objects.all()
    return render(request,'Music/album_view.html',{'artist':artist} )
def track_list(request, pk):
    album = get_object_or_404(Album,pk=pk)
    return render(request,'Music/track_view.html',{'album':album})
def manage_album(request):
    if request.POST:
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Artist_list')
    else:
        form = AlbumForm()
    return render(request, 'Music/manage_albums.html', {'form': form})

def manage_track(request):
    if request.POST:
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track_list')
    else:
        form = TrackForm()
    return render(request, 'Music/manage_track.html', {'form':form})

class ArtistList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ArtistSerializer  
 