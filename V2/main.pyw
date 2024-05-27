# main.py
import customtkinter as ctk
from customtkinter import filedialog
import music_player

# REQUIREMENTS:
# pip3 install customtkinter 
# pip install python-vlc
# pip install --upgrade pip
# You'll need to install the VLC PLAYER from https://www.videolan.org/vlc/


# Initialize the music player
music_player.init_music_player()

def on_select_folder():
    music_player.open_folder(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu)

def on_select_songs():
    music_player.open_songs(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu)

def on_play_or_pause():
    music_player.on_button_play_or_pause(play_pause_button)

def on_stop():
    music_player.on_button_stop(play_pause_button)

def on_next_song():
    music_player.next_song()

def on_previous_song():
    music_player.previous_song(next_button)

def on_check_music():
    music_player.check_music()

def on_repeat_button_label():
    music_player.repeat_button_label(repeat_button)

def optionmenu_callback(choice):
    if choice == "Open Folder":
        on_select_folder()
    elif choice == "Open File(s)":
        on_select_songs()
    print("optionmenu dropdown clicked:", choice)


ctk.set_appearance_mode("dark") # Set dark mode theme globally
root = ctk.CTk()
root.title("Vicyos Music Player")
root.geometry("300x400")


play_pause_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Start Playing the song", command=on_play_or_pause, state=ctk.DISABLED)
play_pause_button.pack(pady=17)

stop_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Stop", command=on_stop, state=ctk.DISABLED)
stop_button.pack(pady=17)

open_files_default = ctk.StringVar(value="Open Folder")
open_files_option_menu = ctk.CTkOptionMenu(root, values=["Open Folder", "Open File(s)"], variable=open_files_default, command=optionmenu_callback)
open_files_option_menu.pack(pady=17)

next_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Next", command=on_next_song, state=ctk.DISABLED)
next_button.pack(pady=17)

previous_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Previous", command=on_previous_song, state=ctk.DISABLED)
previous_button.pack(pady=17)

repeat_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Repeat mode: Off", command=on_repeat_button_label, state=ctk.DISABLED)
repeat_button.pack(pady=17)

root.after(1000, lambda: music_player.repeat_checker(root, play_pause_button, next_button, previous_button))
root.mainloop()