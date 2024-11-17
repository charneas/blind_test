import time
import random
import os
import pytube
from moviepy.editor import AudioFileClip
import pygame
import sqlite3
from configparser import ConfigParser

PATH = 'Globals.ini'

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
    song = Get_Request('GET_SONG')
    song = Execute_Request(song)
    print(song)

if __name__ == '__main__':
    main()

