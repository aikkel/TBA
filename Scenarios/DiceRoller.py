import random
from Media.Sound import SoundPlayer

class DiceRoller:
    def __init__(self, name):
        self.player = None
        self.name = name

    def set_player(self, player):
        self.player = player

    def roll_dice_player(self, num_dice, modifier=0):
        roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + modifier
        return roll_total
    
    def roll_dice_luck(self, player):
        luck_roll = random.randint(2, 12)
        if luck_roll <= player.luck:
            SoundPlayer.play_sound('lucky.wav')
            player.luck -= 1
            print(f"You got lucky! Your luck is now {player.luck}" )
            return "lucky! " + str(player.luck)
        else:
            SoundPlayer.play_sound('unlucky.wav')
            player.luck -= 1
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
            SoundPlayer().play_sound('heroattack.wav')
            if roll_luck:
                luck_result = self.roll_dice_luck(self.player)
                if "lucky" in luck_result:
                    print("Player got lucky! Damage increased.")
                else:
                    print("Player got unlucky! Damage decreased.")
        elif monster_roll > player_roll:
            SoundPlayer().play_sound('orcattack.wav')
            print("Monster wins!")
        else:
            SoundPlayer().play_sound('whoosh.wav')
            print("It's a tie!")
