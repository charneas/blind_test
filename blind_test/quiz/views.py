from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "quiz/index.html")

def NewSong(request):
    return render(request,"./pages/NewSong.html",content_type="application/xhtml+xml")