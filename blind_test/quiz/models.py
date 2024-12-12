from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.country

# Create your models here.
class Song(models.Model):
    Titre = models.CharField(max_length=200)
    Annee = models.IntegerField()
    Interprete = models.CharField(max_length=200)
    Lien = models.CharField(max_length=300)
    Pays = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titre