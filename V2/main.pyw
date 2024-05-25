# main.py
import tkinter as tk
from tkinter import filedialog
import music_player

# Initialize the music player
music_player.init_music_player()

def on_select_folder():
    music_player.selected_folder(filedialog, play_pause_button, stop_button, next_button, previous_button, is_play_button)

def on_play_or_pause():
    music_player.on_button_play_or_pause(play_pause_button)

def on_stop():
    music_player.on_button_stop(play_pause_button)

def on_next_song():
    music_player.next_song()

def on_previous_song():
    music_player.previous_song()

def on_check_music():
    music_player.check_music()

root = tk.Tk()
root.title("Vicyos Music Player")
root.geometry("300x400")

play_pause_button = tk.Button(root, text="Start Playing the song", command=on_play_or_pause, state=tk.DISABLED)
play_pause_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=on_stop, state=tk.DISABLED)
stop_button.pack(pady=20)

is_play_button = tk.Button(root, text="Is there anything playing?", command=on_check_music, state=tk.DISABLED)
is_play_button.pack(pady=20)

select_folder_button = tk.Button(root, text="Open a folder", command=on_select_folder)
select_folder_button.pack(pady=20)

next_button = tk.Button(root, text="Previous", command=on_previous_song, state=tk.DISABLED)
next_button.pack(pady=20)

previous_button = tk.Button(root, text="Next", command=on_next_song, state=tk.DISABLED)
previous_button.pack(pady=20)

root.after(1000, lambda: music_player.music_has_finished(root))
root.mainloop()