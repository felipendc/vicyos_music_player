# music_player.py
import pygame
import os
import tkinter as tk
from enum import Enum

repeat_song = "playlist"
pause_music = False
stop_music = False
music_folder_path = []
song_index = 0

repeat_options = {
    'CURRENT': "current",
    'PLAYLIST': "playlist",
    'NONE': "none",
}


def init_music_player():
    pygame.init()
    pygame.mixer.init()


def selected_folder(filedialog, play_pause_button, stop_button, next_button, previous_button, is_play_button):
    global music_folder_path, song_index

    directory = filedialog.askdirectory()
    if directory:
        music_folder_path.clear()  # Empty the current playlist
        for root_, dirs, files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    path = (root_ + '/' + file).replace('\\', '/')
                    music_folder_path.append(path)

        if len(music_folder_path) > 0:
            song_index = 0
            on_button_stop(play_pause_button)
            on_button_play_or_pause(play_pause_button)
            play_pause_button.config(state=tk.NORMAL)
            stop_button.config(state=tk.NORMAL)
            next_button.config(state=tk.NORMAL)
            previous_button.config(state=tk.NORMAL)
            is_play_button.config(state=tk.NORMAL)
    else:
        pass

def next_song():
    global song_index
    if song_index < len(music_folder_path) - 1:
        song_index += 1
        pygame.mixer.music.load(music_folder_path[song_index])
        pygame.mixer.music.play()
    elif song_index >= len(music_folder_path) - 1:
        if repeat_song == "none":
            pass
    elif song_index >= len(music_folder_path) - 1:
        song_index = 0
        pygame.mixer.music.load(music_folder_path[song_index])
        pygame.mixer.music.play()


def previous_song():
    global song_index
    if song_index > 0:
        song_index -= 1
        pygame.mixer.music.load(music_folder_path[song_index])
        pygame.mixer.music.play()
    else:
        song_index = 0

def on_button_play_or_pause(play_pause_button):
    global pause_music, music_folder_path, stop_music

    if not pygame.mixer.music.get_busy() and pause_music == False:
        pygame.mixer.music.load(music_folder_path[song_index])
        pygame.mixer.music.play()
        stop_music = False
        play_pause_button.config(text="Pause")
    elif pause_music == False:
        pygame.mixer.music.pause()
        pause_music = True
        play_pause_button.config(text="Play")
    elif pause_music == True:
        pygame.mixer.music.unpause()
        pause_music = False
        play_pause_button.config(text="Pause")

def on_button_stop(play_pause_button):
    global pause_music, stop_music
    pygame.mixer.music.stop()
    pause_music = False
    stop_music = True
    play_pause_button.config(text="Start Playing the song")

def check_music():
    global music_folder_path

    if not pygame.mixer.music.get_busy() and pause_music == False:
        print("There is nothing being played at the moment...")
    elif not pygame.mixer.music.get_busy() and pause_music == True:
        print("The song is currently paused!")
    else:
        print("There is a song being played at the moment...")

def repeat_checker(root):
    global music_folder_path, repeat_song

    if not pygame.mixer.music.get_busy() and pause_music == False:
        if repeat_song == "playlist":
            if len(music_folder_path) > 0 and not stop_music:
                next_song()
            print("REPEAT_PLAYLIST")

        elif repeat_song == "current":
            if len(music_folder_path) > 0:
                pygame.mixer.music.load(music_folder_path[song_index])
                pygame.mixer.music.play()
            print("REPEAT_CURRENT")

        elif repeat_song == "none":
            if len(music_folder_path) > 0:
                pass
                # if song_index >= len(music_folder_path) - 1:
            print("REPEAT_NONE")

        # elif not pygame.mixer.music.get_busy() and pause_music == True:
        #     print("The song is currently paused!")
        # else:
        #     print("Playing: " + music_folder_path[song_index])

    root.after(1000, lambda: repeat_checker(root))