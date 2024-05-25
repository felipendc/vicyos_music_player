import pygame # pip install pygame
import tkinter as tk
from tkinter import filedialog
import os

repeat_song = 0 # This feature will be implemented in the future!
pause_music = False
stop_music = False
music_folder_path = []
song_index = 0

pygame.init()
pygame.mixer.init()


def selected_folder():
    global music_folder_path, song_index

    directory = filedialog.askdirectory()
    if directory:
        music_folder_path.clear() # Empty the current playlist
        for root_, dirs, files in os.walk(directory):
                for file in files:
                    if os.path.splitext(file)[1] == '.mp3':
                        path = (root_ + '/' + file).replace('\\','/')
                        music_folder_path.append(path)
                        
        if len(music_folder_path) > 0:
            song_index = 0
            on_button_stop()
            on_button_play_or_pause()
            play_pause_button.config(state=tk.NORMAL)
            stop_button.config(state=tk.NORMAL)
            next_button.config(state=tk.NORMAL)
            previous_button.config(state=tk.NORMAL)
            is_play_button.config(state=tk.NORMAL)
    else:
        # Using "pass" to avoid any errors
        pass
       
def next_song():
    global song_index
    if song_index < len(music_folder_path) -1:
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


def on_button_play_or_pause():
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

        
def on_button_stop():
    global pause_music, stop_music
    pygame.mixer.music.stop()
    pause_music == False
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
        

def music_has_finished():
    global music_folder_path

    if not pygame.mixer.music.get_busy() and pause_music == False:
        if len(music_folder_path) > 0 and not stop_music:
            next_song()
        # print("There is nothing being played at the moment...")
    elif not pygame.mixer.music.get_busy() and pause_music == True:    
        print("The song is currently paused!")
    
    else:
        print("Playing: " + music_folder_path[song_index])
        

    root.after(1000, music_has_finished)
        
        
        
#--------------------#
root = tk.Tk()
root.title("Vicyos Music Player")
root.geometry("300x400")


play_pause_button = tk.Button(root, text="Start Playing the song", command=on_button_play_or_pause, state=tk.DISABLED)
play_pause_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=on_button_stop, state=tk.DISABLED)
stop_button.pack(pady=20)

is_play_button = tk.Button(root, text="Is there anything playing?", command=check_music, state=tk.DISABLED)
is_play_button.pack(pady=20)

select_folder_button = tk.Button(root, text="Open a folder", command=selected_folder)
select_folder_button.pack(pady=20)

next_button = tk.Button(root, text="Previous", command=previous_song, state=tk.DISABLED)
next_button.pack(pady=20)

previous_button = tk.Button(root, text="Next", command=next_song, state=tk.DISABLED)
previous_button.pack(pady=20)



#--------------------#
root.after(1000, music_has_finished) 
root.mainloop()