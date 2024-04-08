import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Game import Game
from Units.Player import Player
from Maps.Rooms import all_rooms
from Media.Sound import SoundPlayer
from Scenarios.DiceRoller import DiceRoller

def main():
    # Create a sound player instance
    sound_player = SoundPlayer()
    # Create a player instance
    player = Player("Player 1", sound_player)
    player.update_current_room('0')  # Sets the initial current room to c1

    # Create a game instance
    game_instance = Game(sound_player)

    # Create a dice roller instance with the sound player
    dice_roller = DiceRoller("Dice Roller", sound_player)

    # Call the RunGame function to start the game
    game_instance.RunGame(player, all_rooms)

if __name__ == "__main__":
    main()
