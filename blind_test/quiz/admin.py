from django.contrib import admin
from .models import Country, Song

admin.site.register(Song)
admin.site.register(Country)

