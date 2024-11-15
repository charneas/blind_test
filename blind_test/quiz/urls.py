from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("quiz/", views.index, name="index"),
    path("quiz/NewSong", views.NewSong, name="NewSong"),
]