from django.shortcuts import render
from django.template import RequestContext
from django import forms
from .models import Song

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
    else:
        return render(request, "quiz/index.html")

