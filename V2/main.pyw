# main.py
import customtkinter as ctk # pip3 install customtkinter, pip install --upgrade pip
from customtkinter import filedialog
import music_player

# Initialize the music player
music_player.init_music_player()

def on_select_folder():
    music_player.selected_folder(filedialog, play_pause_button, stop_button, next_button, previous_button, is_play_button, repeat_button, select_folder_button)

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

def on_repeat_button_label():
    music_player.repeat_button_label(repeat_button)


ctk.set_appearance_mode("dark") # Set dark mode theme globally
root = ctk.CTk()
root.title("Vicyos Music Player")
root.geometry("300x470")


play_pause_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Start Playing the song", command=on_play_or_pause, state=ctk.DISABLED)
play_pause_button.pack(pady=20)

stop_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Stop", command=on_stop, state=ctk.DISABLED)
stop_button.pack(pady=20)

is_play_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Is there anything playing?", command=on_check_music, state=ctk.DISABLED)
is_play_button.pack(pady=20)

select_folder_button = ctk.CTkButton(root, fg_color="#666666", hover_color="#777777", text="Open a folder", command=on_select_folder)
select_folder_button.pack(pady=20)

next_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Previous", command=on_previous_song, state=ctk.DISABLED)
next_button.pack(pady=20)

previous_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Next", command=on_next_song, state=ctk.DISABLED)
previous_button.pack(pady=20)

repeat_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Repeat mode: Off", command=on_repeat_button_label, state=ctk.DISABLED)
repeat_button.pack(pady=20)

root.after(1000, lambda: music_player.repeat_checker(root, play_pause_button))
root.mainloop()