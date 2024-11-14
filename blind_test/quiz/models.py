from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.country_text

# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=200)
    song_yeardate = models.IntegerField()
    song_writer = models.CharField(max_length=200)
    song_origin = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_text