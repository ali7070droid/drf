from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

#class Artist(models.Model):
#    artist_name=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#    def __str__(self):
#        return '%s' % (self.artist_name)

class Album(models.Model):
    album_name=models.CharField(max_length=100)
    artist = models.ForeignKey(User,related_name='album', on_delete=models.CASCADE)
    orderA=models.IntegerField()

    def __str__(self):
        return '%s' % (self.album_name)


class Track(models.Model):
    title=models.CharField(max_length=100)
    duration=models.IntegerField()
    album = models.ForeignKey(Album, related_name='track', on_delete=models.CASCADE)
    artist_feat = models.ManyToManyField(User, related_name='feat' ,blank=True, null=True)
    orderT=models.IntegerField()

    class Meta:
        ordering=['orderT']

    def __str__(self):
        #if artist_feat:
        #    return '%s feat. %s' % (self.title) % (self.artist_feat.username)
        #else:
            return '%s' % (self.title)
         