import time
import random
import os
import pytube
from moviepy.editor import AudioFileClip
import pygame
import sqlite3
from configparser import ConfigParser
from pytube import YouTube

PATH = 'Globals.ini'

class chose_song():
    def Get_Request(req):
        config = ConfigParser()
        config.read(PATH)
        value = config.get(req,'request')
        return(value)

    def Execute_Request(request):
        conn = sqlite3.connect(database= 'blind_test\db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(request)
        result = cursor.fetchone()
        return(result)

    def main():
        song = chose_song.Get_Request('GET_SONG')
        song = chose_song.Execute_Request(song)  
        return(song)

class download_music():
    def download(url):
        yt = YouTube(url)
        filename = 'TemporaryName.Mp4'
        music = yt.streams.filter(only_audio=True).first().download(output_path='blind_test\quiz\Temp', filename='TemporaryName.Mp4')
        return(music, filename)

