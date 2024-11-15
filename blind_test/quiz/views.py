from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class NewSongForms(forms.Form):
    song_title = forms.CharField(max_length=200)
    song_yeardate = forms.IntegerField()
    song_writer = forms.CharField(max_length=200)
    song_origin = forms.CharField(max_length=30)
    song_link = forms.CharField(max_length=300)

def index(request):
    return render(request, "quiz/index.html")

def NewSong(request):
    context = {}
    context['NewSongForm'] = NewSongForms
    return render(request,"./quiz/NewSong.html",context)