from django.shortcuts import render
from django.template import RequestContext
from django import forms
from .models import Song
from .core.blindtest import chose_song, download_music

class NewSongForms(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"

def AddSong(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = NewSongForms(request.POST)
        
    if form.is_valid():
        form.save(commit=True)
        return render(request, "quiz/Newsong_success.html")

def index(request):
    if 'NewSong' in request.POST:
        context = {'form' : NewSongForms()}
        return render(request,"./quiz/NewSong.html",context)
    if 'AddSong' in request.POST:
        AddSong(request)
    if 'Join' in request.POST:
        song = chose_song.main()[3]
        #song_path, filename = download_music.download(song)
        #song_path = 'http://127.0.0.1:8000/quiz/TemporaryName.Mp4'
        context = {'url' : song}
        return render(request, 'quiz/play_song.html', context)
    else:
        return render(request, "quiz/index.html")

