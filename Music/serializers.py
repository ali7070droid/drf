from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Track, Album

#class ArtistSerializer(serializers.ModelSerializer):
#
#    #album = serializers.StringRelatedField(many=True)
#
#    class Meta:
#        model = User
#        fields = ['username']

#class AlbumSerializer(serializers.ModelSerializer):
#    album = ArtistSerializer(many=True, read_only=True)
#    class Meta:
#        model = Album
#        fields = ['album_name', 'album']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['title']

class AlbumSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True, read_only=True)
    class Meta:
        model=Album
        fields=['album_name', 'track']

class ArtistSerializer(serializers.ModelSerializer):
    album=AlbumSerializer(many=True, read_only=True)
    class Meta:
        model=User
        fields=['username', 'album']

