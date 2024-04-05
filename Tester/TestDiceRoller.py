import sys
import os

# Add the parent directory of 'Scenarios' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import MagicMock
from Scenarios.DiceRoller import DiceRoller
from Units.Player import Player
from Units.Monster import retrieve_monsters_from_db

class TestDiceRoller(unittest.TestCase):
    def setUp(self):
        # Mocking SoundPlayer object as it's not required for these tests
        sound_player = MagicMock()
        # Creating a Player instance for testing
        player = Player("Test Player")
        # Retrieving monsters from the database
        art_reader = None  # You might need to provide an ArtReader object here
        monsters = retrieve_monsters_from_db('monsters.db', art_reader)
        # For simplicity, let's assume you want the first monster from the database
        monster = monsters.get(1)
        self.dice_roller = DiceRoller("Player", sound_player)
        self.dice_roller.set_player(player)
        self.dice_roller.set_monster(monster)  # Passing the monster object to DiceRoller
        

    # def test_conduct_battle_player_wins(self):
    #     self.dice_roller.conduct_battle(1)

    # def test_conduct_battle_monster_wins(self):
    #     self.dice_roller.conduct_battle(1)

    # def test_conduct_battle_tie(self):
    #     self.dice_roller.conduct_battle(1)
    def test_conduct_battle_player_wins(self):
        self.dice_roller.conduct_battle()

    def test_conduct_battle_monster_wins(self):
        self.dice_roller.conduct_battle()

    def test_conduct_battle_tie(self):
        self.dice_roller.conduct_battle()

if __name__ == '__main__':
    unittest.main()

