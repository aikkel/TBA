import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random

# Assuming the Media folder is in the same directory as this script
from Media.Sound import SoundPlayer  # Assuming SoundPlayer is implemented correctly

class DiceRoller:
    def __init__(self, name, sound_player):
        self.player = None
        self.name = name
        self.sound_player = sound_player  # Store the SoundPlayer instance

    def set_player(self, player):
        self.player = player

    def roll_dice_player(self, num_dice, modifier=0):
        roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + modifier
        return roll_total

    def roll_dice_luck(self, player):
        luck_roll = random.randint(2, 12)
        if luck_roll <= player.luck:
            self.sound_player.play_sound('lucky.wav')  # Use the stored SoundPlayer instance
            player.luck -= 1
            print(f"You got lucky! Your luck is now {player.luck}")
            return "lucky! " + str(player.luck)
        else:
            self.sound_player.play_sound('unlucky.wav')  # Use the stored SoundPlayer instance
            player.luck -= 1
            print("You got unlucky! Damage decreased.")
            return "unlucky!"

    def roll_dice_battle(self, num_dice, skill):
        roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + skill
        return roll_total

    def conduct_battle(self, monster, roll_luck=False):
        player_roll = self.roll_dice_battle(2, self.player.skill)
        monster_roll = self.roll_dice_battle(2, monster.skill)

        print(f"Player rolled {player_roll}. Monster rolled {monster_roll}.")

        if player_roll > monster_roll:
            print("Player wins!")
            self.sound_player.play_sound('heroattack.wav')  # Use the stored SoundPlayer instance
            if roll_luck:
                luck_result = self.roll_dice_luck(self.player)
                if "lucky" in luck_result:
                    print("Player got lucky! Damage increased.")
                else:
                    print("Player got unlucky! Damage decreased.")
        elif monster_roll > player_roll:
            self.sound_player.play_sound('orcattack.wav')  # Use the stored SoundPlayer instance
            print("Monster wins!")
        else:
            self.sound_player.play_sound('whoosh.wav')  # Use the stored SoundPlayer instance
            print("It's a tie!")

# Assuming you have instantiated SoundPlayer somewhere in your main program
# sound_player = SoundPlayer()

# Then you can create a DiceRoller instance like this
# dice_roller = DiceRoller("Player", sound_player)
