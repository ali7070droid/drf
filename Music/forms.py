from django import forms
from .models import Album, Track

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist')

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('title', 'duration', 'album', 'artist_feat')