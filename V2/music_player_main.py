import pygame # pip install pygame
import tkinter as tk
from music_player_functions import *
from music_player_variables import *


pygame.init()
pygame.mixer.init()


#---------GUI-----------#
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