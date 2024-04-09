import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading
from time import sleep
from Game import Game
from Units.Player import Player
from Maps.Rooms import all_rooms
from Media.Sound import SoundPlayer

def main(sound_player, sound_lock):
    player = Player("Player 1", sound_player)
    player.update_current_room('0')

    game_instance = Game(sound_player, sound_lock)  # Pass the sound lock to the Game instance

    game_instance.RunGame(player, all_rooms)

    return player

def play_background_sounds(sound_player):
    while True:
        sound_player.play_titel()
        sleep(32)

if __name__ == "__main__":
    sound_player = SoundPlayer()
    sound_lock = threading.Lock()  # Create a lock for SoundPlayer access

    background_music_thread = threading.Thread(target=play_background_sounds, args=(sound_player,))
    background_music_thread.daemon = True
    background_music_thread.start()

    game_thread = threading.Thread(target=main, args=(sound_player, sound_lock))  # Pass the SoundPlayer object and lock to the game thread
    game_thread.start()

    game_thread.join()

    sound_player.stop_music_loop_thread()
