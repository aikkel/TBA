import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Game import Game
from Units.Player import Player
from Maps.Rooms import all_rooms
from Media.Sound import SoundPlayer

def main():
    # Create a player instance
    player = Player("Player 1")
    player.update_current_room('0')  # Sets the initial current room to c1
    sound_player = SoundPlayer()

    # Create a game instance
    game_instance = Game(sound_player)


    # Call the RunGame function to start the game
    game_instance.RunGame(player, all_rooms)

if __name__ == "__main__":
    main()