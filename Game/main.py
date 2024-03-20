import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Game import Game
def main():
    # Create a new game instance
    game_instance = Game()

    # Start the game loop or perform other actions
    # For example:
    # game_instance.start_game()

if __name__ == "__main__":
    main()