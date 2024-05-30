# main.py
import customtkinter as ctk
from customtkinter import filedialog
import music_player

# REQUIREMENTS:
# pip3 install customtkinter 
# pip install python-vlc
# pip install --upgrade pip
# You'll need to install the VLC PLAYER from https://www.videolan.org/vlc/
# pip install keyboard
# pip install pycaw


# Initialize the music player
music_player.init_music_player()

def on_up_arrow_pressed(event):
    music_player.increase_volume()

def on_down_arrow_pressed(event):
    music_player.decrease_volume()

def on_left_arrow_pressed(event):
    music_player.rewind()
    print("Left arrow key pressed")

def on_right_arrow_pressed(event):
    music_player.forward()
    print("Right arrow key pressed")

def on_space_pressed(event):
    print("button was pressed")
    music_player.on_button_play_or_pause(play_pause_button)

def on_select_folder():
    music_player.open_folder(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu, set_time_rewind_button, set_time_skip_forward_button)

def on_select_songs():
    music_player.open_songs(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu, set_time_rewind_button, set_time_skip_forward_button)

def on_add_to_playlist():
    music_player.add_to_playlist(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu, set_time_rewind_button, set_time_skip_forward_button)

def on_play_or_pause():
    music_player.on_button_play_or_pause(play_pause_button)

def on_stop():
    music_player.on_button_stop(play_pause_button)

def on_next_song():
    music_player.next_song(play_pause_button)

def on_previous_song():
    music_player.previous_song(next_button, play_pause_button)

def on_check_music():
    music_player.check_music()

def on_repeat_button_label():
    music_player.repeat_button_label(repeat_button)

def on_optionmenu_callback(choice):
    if choice == "Open Folder":
        on_select_folder()
    elif choice == "Open File(s)":
        on_select_songs()
    elif choice == "Add to Playlist":
        print(choice)
        on_add_to_playlist()
    print("optionmenu dropdown clicked:", choice)

def on_speed_combobox_callback(choice):
    music_player.playback_speed(choice)
    print("combobox dropdown clicked:", choice)
    
def on_choose_playback_speed():
    return music_player.playback_speed_list

def on_rewind():
    music_player.rewind()

def on_forward():
    music_player.forward()

ctk.set_appearance_mode("dark") # Set dark mode theme globally
root = ctk.CTk()
root.title("Vicyos Music Player")
root.geometry("300x570")


play_pause_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Play", command=on_play_or_pause, state=ctk.DISABLED)
play_pause_button.pack(pady=14)

stop_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Stop", command=on_stop, state=ctk.DISABLED)
stop_button.pack(pady=14)

open_files_default = ctk.StringVar(value="Open Folder")
open_files_option_menu = ctk.CTkOptionMenu(root, values=["Open Folder", "Open File(s)", "Add to Playlist"], variable=open_files_default, command=on_optionmenu_callback)
open_files_option_menu.pack(pady=14)

next_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Next", command=on_next_song, state=ctk.DISABLED)
next_button.pack(pady=14)

previous_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Previous", command=on_previous_song, state=ctk.DISABLED)
previous_button.pack(pady=14)

repeat_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Repeat mode: Off", command=on_repeat_button_label, state=ctk.DISABLED)
repeat_button.pack(pady=14)

spaced_box_label = ctk.CTkLabel(root, text="", fg_color="transparent")
spaced_box_label.pack(pady=0)
playback_speed_label = ctk.CTkLabel(root, text="Speed Rate:", fg_color="transparent")
playback_speed_label.pack(pady=0, expand=False)
speed_combobox_var = ctk.StringVar(value="1.0")
playback_speed_combobox = ctk.CTkComboBox(root, variable=speed_combobox_var, values=on_choose_playback_speed(),
                                     command=on_speed_combobox_callback)
playback_speed_combobox.pack(pady=5)

set_time_rewind_button = ctk.CTkButton(root, fg_color="#444444", hover_color="#555555", text="Rewind 5 seconds", command=on_rewind, state=ctk.DISABLED)
set_time_rewind_button.pack(pady=5 )

set_time_skip_forward_button = ctk.CTkButton(root,  fg_color="#444444", hover_color="#555555", text="Forward 5 seconds", command=on_forward, state=ctk.DISABLED)
set_time_skip_forward_button.pack(pady=5)
# Rewind and skip forward
root.after(500, lambda: music_player.repeat_checker(root, play_pause_button, next_button, previous_button))

# Bind the space key press event to the function space_pressed
root.bind("<space>", on_space_pressed)
root.bind("<Left>", on_left_arrow_pressed)
root.bind("<Right>", on_right_arrow_pressed)
root.bind("<Up>", on_up_arrow_pressed)
root.bind("<Down>", on_down_arrow_pressed)

root.mainloop()