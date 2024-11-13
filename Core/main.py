import random
import time
import os
from pytube import Playlist, YouTube
from moviepy.editor import AudioFileClip
from configparser import ConfigParser
import pygame

def GetConfigValue(path,value):
    config = ConfigParser()
    config.read(path)
    value = config.get('GLOBALS',value)
    return(value)


if __name__ == '__main__':
    configfilepath = '../Globals.ini'
    playlist = 'PLAYLIST_URL'
    playlist_url = GetConfigValue(configfilepath,playlist)

    print(playlist_url)