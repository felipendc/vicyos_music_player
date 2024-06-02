# music_player.py
import vlc, os
import customtkinter as ctk
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


repeat_options = {
    "NONE": "none",
    "CURRENT": "current",
    "PLAYLIST": "playlist",
}


repeat_song = repeat_options["NONE"]
pause_music = False
stop_music = False
music_folder_path = []
song_index = 0
playback_speed_list = ["1.6", "1.5", "1.4", "1.3", "1.2", "1.1", "1.0", "0.99", "0.98", "0.97", "0.96", "0.95", "0.94", "0.93", "0.92", "0.91", "0.90"]
playback_speed_var = 1.0


def increase_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(1.0, current_volume + 0.1), None)  # Increase by 10%, ensuring it doesn't exceed 1.0

# Function to decrease the system volume
def decrease_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(0.0, current_volume - 0.1), None)  # Decrease by 10%, ensuring it doesn't go below 0.0

def rewind():
    player.set_time(player.get_time() - 5000)

def forward():
    player.set_time(player.get_time() + 5000)

def playback_speed(choice):
    global playback_speed_var 
    playback_speed_var = float(choice)
    
def init_music_player():
    # Creating VLC instance
    global instance, player
    instance = vlc.Instance()

    # Creating VLC media player
    player = instance.media_player_new()

def add_to_playlist(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu, set_time_rewind_button, set_time_skip_forward_button):
    global music_folder_path, song_index

    dialog_title = "Open"
    initial_directory = os.path.expanduser("~/Music")
    supported_extensions = ["*.m4a*", "*.mp3*"]
    
    selected_songs = filedialog.askopenfilenames(
        initialdir=initial_directory,
        filetypes=[("All files", supported_extensions), (".mp3", "*.mp3"), (".m4a", "*.m4a*")],
        title=dialog_title
    )

    playlist_is_empty = True
    if len(music_folder_path) > 0:
        playlist_is_empty = False
    else:
        playlist_is_empty = True

    if not playlist_is_empty:

        if not selected_songs:
            print("NOTHING HAS BEEN SELECTED!")
        else:
            # Convert tuple to list
            music_folder_path_to_list = list(music_folder_path)
            selected_songs_to_list = list(selected_songs)
            temp_list =[]
            
            for files in music_folder_path_to_list:
                temp_list.append(files)

            for files in selected_songs_to_list:
                temp_list.append(files)
            
            music_folder_path = []
            for files in temp_list:
                music_folder_path.append(files)

    else:
        # Convert tuple to list
        selected_songs_to_list = list(selected_songs)
        for files in selected_songs_to_list:
            music_folder_path.append(files)

        print("PLAY LIST IS FULLY EMPTY")
        song_index = 0
        media = instance.media_new(music_folder_path[song_index])
        player.set_media(media)
        on_button_stop(play_pause_button)
        on_button_play_or_pause(play_pause_button)
        play_pause_button.configure(state=ctk.NORMAL)
        stop_button.configure(state=ctk.NORMAL)
        next_button.configure(state=ctk.NORMAL)
        previous_button.configure(state=ctk.NORMAL)
        repeat_button.configure(state=ctk.NORMAL)
        open_files_option_menu.configure( fg_color=("#666666"), button_color="#444444", button_hover_color="#888888")
        set_time_rewind_button.configure(state=ctk.NORMAL)
        set_time_skip_forward_button.configure(state=ctk.NORMAL)
        


def open_songs(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu, set_time_rewind_button, set_time_skip_forward_button):
    global music_folder_path, song_index

    dialog_title = "Open"
    initial_directory = os.path.expanduser("~/Music")
    supported_extensions = ["*.m4a*", "*.mp3*"]
    
    selected_songs = filedialog.askopenfilenames(
        initialdir=initial_directory,
        filetypes=[("All files", supported_extensions), (".mp3", "*.mp3"), (".m4a", "*.m4a*")],
        title=dialog_title
    )
    if not selected_songs:
        print("NOTHING HAS BEEN SELECTED!")
    else:
        music_folder_path = []
        music_folder_path = selected_songs

        if len(music_folder_path) > 0:
            # print(music_folder_path)
            song_index = 0
            media = instance.media_new(music_folder_path[song_index])
            player.set_media(media)
            on_button_stop(play_pause_button)
            on_button_play_or_pause(play_pause_button)
            play_pause_button.configure(state=ctk.NORMAL)
            stop_button.configure(state=ctk.NORMAL)
            next_button.configure(state=ctk.NORMAL)
            previous_button.configure(state=ctk.NORMAL)
            repeat_button.configure(state=ctk.NORMAL)
            open_files_option_menu.configure( fg_color=("#666666"), button_color="#444444", button_hover_color="#888888")
            set_time_rewind_button.configure(state=ctk.NORMAL)
            set_time_skip_forward_button.configure(state=ctk.NORMAL)
        else:
            pass


def open_folder(filedialog, play_pause_button, stop_button, next_button, previous_button, repeat_button, open_files_option_menu, set_time_rewind_button, set_time_skip_forward_button):
    global music_folder_path, song_index

    dialog_title = "Select a Directory"
    suported_files_extensions = [".mp3", ".m4a"]
    directory = filedialog.askdirectory(title=dialog_title)

    if directory:
        music_folder_path = []  # Empty the current playlist

        for root_, dirs, files in os.walk(directory):
            for file in files:
                for suported_extensions in suported_files_extensions:
                    # print(suported_extensions)
                    if os.path.splitext(file)[1].lower() == suported_extensions:
                        path = (root_ + "/" + file).replace("\\", "/")
                        music_folder_path.append(path)
                    
        if len(music_folder_path) > 0:
            # print(music_folder_path)
            song_index = 0
            media = instance.media_new(music_folder_path[song_index])
            player.set_media(media)
            on_button_stop(play_pause_button)
            on_button_play_or_pause(play_pause_button)
            play_pause_button.configure(state=ctk.NORMAL)
            stop_button.configure(state=ctk.NORMAL)
            next_button.configure(state=ctk.NORMAL)
            previous_button.configure(state=ctk.NORMAL)
            repeat_button.configure(state=ctk.NORMAL)
            open_files_option_menu.configure( fg_color=("#666666"), button_color="#444444", button_hover_color="#888888")
            set_time_rewind_button.configure(state=ctk.NORMAL)
            set_time_skip_forward_button.configure(state=ctk.NORMAL)
    else:
        pass


def next_song(play_pause_button):
    global song_index, stop_music, pause_music
    if song_index < len(music_folder_path) - 1:
        song_index += 1
        media = instance.media_new(music_folder_path[song_index])
        player.set_media(media)
        player.play()
        pause_music = False
        stop_music = False
        if not play_pause_button.configure(text="Pause"):
            play_pause_button.configure(text="Pause")
    
    elif song_index >= len(music_folder_path) - 1 and repeat_song == repeat_options["PLAYLIST"]:
        song_index = 0
        media = instance.media_new(music_folder_path[song_index])
        player.set_media(media)
        player.play()
        if not play_pause_button.configure(text="Pause"):
            play_pause_button.configure(text="Pause")
    else:
        pass

def previous_song(next_button, play_pause_button):
    global song_index, stop_music
    if song_index > 0:
        song_index -= 1
        media = instance.media_new(music_folder_path[song_index])
        player.set_media(media)
        player.play()
        stop_music = False
        if not play_pause_button.configure(text="Pause"):
            play_pause_button.configure(text="Pause")

        if song_index < len(music_folder_path) - 1:
            next_button.configure(state=ctk.NORMAL)

    else:
        song_index = 0


def on_button_play_or_pause(play_pause_button):
    global pause_music, music_folder_path, stop_music

    if player.get_state() == vlc.State.Playing:
        player.pause()
        pause_music = True
        stop_music = False
        play_pause_button.configure(text="Play")

    elif player.get_state() == vlc.State.Paused:
        player.play()
        pause_music = False
        play_pause_button.configure(text="Pause")


    elif player.get_state() == vlc.State.Stopped:
        player.play()
        pause_music = False
        stop_music = False
        play_pause_button.configure(text="Pause")


def on_button_stop(play_pause_button):
    global pause_music, stop_music
    player.stop()
    pause_music = False
    stop_music = True
    play_pause_button.configure(text="Play")


def repeat_checker(root, play_pause_button, next_button, previous_button, current_timestamp_label, song_lenght_label):
    global music_folder_path, repeat_song, stop_music

    
    
    
    
    if player.get_state() == vlc.State.Playing or player.get_state() == vlc.State.Paused:
        # Convert seconds to minutes and seconds
        current_time = player.get_time() / 1000
        current_time_min = int(current_time // 60)
        current_time_secs = int(current_time % 60)
        print(f"Current Time: {current_time_min:02} minutes and {current_time_secs:02} seconds.")
        current_timestamp_label.configure(text=f"Current time: {current_time_min:02}:{current_time_secs:02}")

        media_length_seconds = player.get_length() / 1000
        song_lenght_minutes = int(media_length_seconds // 60)
        song_lenght_seconds = int(media_length_seconds % 60)
        song_lenght_label.configure(text=f"Full lenght:  {song_lenght_minutes:02}:{song_lenght_seconds:02}")
        print(f"Audio Length: {song_lenght_minutes:02} minutes and {song_lenght_seconds:02} seconds.")

    else:
        current_timestamp_label.configure(text=f"Current Time: 00:00")
        song_lenght_label.configure(text=f"Full lenght: 00:00")

        
    player.set_rate(playback_speed_var)

    if song_index == 0:
        previous_button.configure(state=ctk.DISABLED)
    if song_index > 0:
        previous_button.configure(state=ctk.NORMAL)

    if song_index < len(music_folder_path) - 1:
        next_button.configure(state=ctk.NORMAL)

    if repeat_song == repeat_options["PLAYLIST"]:
        next_button.configure(state=ctk.NORMAL)

    if song_index > len(music_folder_path) - 2:
        next_button.configure(state=ctk.DISABLED)

    if repeat_song == repeat_options["PLAYLIST"] and song_index > len(music_folder_path) - 2:
        next_button.configure(state=ctk.NORMAL)

    if player.get_state() == vlc.State.Ended and pause_music == False:
        if repeat_song == repeat_options["PLAYLIST"]:
          
            if len(music_folder_path) > 0 and stop_music == False:
                next_song(play_pause_button)

        elif repeat_song == repeat_options["CURRENT"]:

            if len(music_folder_path) > 0:
                media = instance.media_new(music_folder_path[song_index])
                player.set_media(media)
                player.play()
            # Printing to debug the code!
        elif repeat_song == repeat_options["NONE"]:
            if len(music_folder_path) > 0:
                player.stop()
                stop_music = True
                play_pause_button.configure(text="Play")
                pass

    root.after(500, lambda: repeat_checker(root, play_pause_button, next_button, previous_button, current_timestamp_label, song_lenght_label ))
        

def repeat_button_label(repeat_button):
    global repeat_song
    if repeat_song == repeat_options["NONE"]:
        # print(repeat_song) # Printing to debug the code!
        repeat_button.configure(text="Repeat: Current song")
        repeat_song = repeat_options["CURRENT"]
        # print(repeat_song) # Printing to debug the code!
    elif repeat_song == repeat_options["CURRENT"]:
        # print(repeat_song) # Printing to debug the code!
        repeat_button.configure(text="Repeat: Playlist")
        repeat_song = repeat_options["PLAYLIST"]
        # print(repeat_song) # Printing to debug the code!
    elif repeat_song == repeat_options["PLAYLIST"]:
        # print(repeat_song) # Printing to debug the code!
        repeat_button.configure(text="Repeat mode: Off")
        repeat_song = repeat_options["NONE"]
        # print(repeat_song) # Printing to debug the code!

