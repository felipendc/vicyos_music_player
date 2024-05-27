# music_player.py
import pygame
import os
import customtkinter as ctk


repeat_options = {
    'NONE': "none",
    'CURRENT': "current",
    'PLAYLIST': "playlist",
}

repeat_song = repeat_options["NONE"]
pause_music = False
stop_music = False
music_folder_path = []
song_index = 0


def init_music_player():
    pygame.init()
    pygame.mixer.init()


def selected_folder(filedialog, play_pause_button, stop_button, next_button, previous_button, is_play_button, repeat_button, select_folder_button):
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
            play_pause_button.configure(state=ctk.NORMAL)
            stop_button.configure(state=ctk.NORMAL)
            next_button.configure(state=ctk.NORMAL)
            previous_button.configure(state=ctk.NORMAL)
            is_play_button.configure(state=ctk.NORMAL)
            repeat_button.configure(state=ctk.NORMAL)
            select_folder_button.configure(fg_color="#444444", hover_color="#555555",)
    else:
        pass


def next_song():
    global song_index
    if song_index < len(music_folder_path) - 1:
        song_index += 1
        pygame.mixer.music.load(music_folder_path[song_index])
        pygame.mixer.music.play()
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
        play_pause_button.configure(text="Pause")
    elif pause_music == False:
        pygame.mixer.music.pause()
        pause_music = True
        play_pause_button.configure(text="Play")
    elif pause_music == True:
        pygame.mixer.music.unpause()
        pause_music = False
        play_pause_button.configure(text="Pause")

def on_button_stop(play_pause_button):
    global pause_music, stop_music
    pygame.mixer.music.stop()
    pause_music = False
    stop_music = True
    play_pause_button.configure(text="Start Playing the song")

def check_music():
    global music_folder_path
    if not pygame.mixer.music.get_busy() and pause_music == False:
        print("There is nothing being played at the moment...")
    elif not pygame.mixer.music.get_busy() and pause_music == True:
        print("The song is currently paused!")
    else:
        print("There is a song being played at the moment...")


def repeat_checker(root, play_pause_button):
    global music_folder_path, repeat_song
    if not pygame.mixer.music.get_busy() and pause_music == False:
        if repeat_song == "playlist":
            if len(music_folder_path) > 0 and not stop_music:
                next_song()
            print(repeat_song) # Printing to debug the code!
        elif repeat_song == "current":
            if len(music_folder_path) > 0:
                pygame.mixer.music.load(music_folder_path[song_index])
                pygame.mixer.music.play()
            print(repeat_song) # Printing to debug the code!
        elif repeat_song == "none":
            if len(music_folder_path) > 0:
                play_pause_button.configure(text="Play")
                # play_pause_button.configure(text="Play")
                pass
            print(repeat_song) # Printing to debug the code!
    root.after(1000, lambda: repeat_checker(root, play_pause_button))
        

def repeat_button_label(repeat_button):
    global repeat_song
    if repeat_song == repeat_options["NONE"]:
        print(repeat_song) # Printing to debug the code!
        repeat_button.configure(text="Repeat: Current song")
        repeat_song = repeat_options["CURRENT"]
        print(repeat_song) # Printing to debug the code!
    elif repeat_song == repeat_options["CURRENT"]:
        print(repeat_song) # Printing to debug the code!
        repeat_button.configure(text="Repeat: Playlist")
        repeat_song = repeat_options["PLAYLIST"]
        print(repeat_song) # Printing to debug the code!
    elif repeat_song == repeat_options["PLAYLIST"]:
        print(repeat_song) # Printing to debug the code!
        repeat_button.configure(text="Repeat mode: Off")
        repeat_song = repeat_options["NONE"]
        print(repeat_song) # Printing to debug the code!