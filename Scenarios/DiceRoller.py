import random

# from Media.Sound import SoundPlayer
# from Units.Monster import Monster

class DiceRoller:
    def __init__(self, name, sound_player):
        self.player = None
        self.name = name
        self.sound_player = sound_player  # Store the SoundPlayer instance
        self.monster = None

    def set_player(self, player):
        self.player = player

    def set_monster(self, monster):
        self.monster = monster

    def roll_dice_player(self, num_dice, modifier=0):
        roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + modifier
        return roll_total

    def roll_dice_luck(self, player):
        luck_roll = random.randint(2, 12)
        if luck_roll <= player.luck:
            self.sound_player.play_sound('lucky.wav')  # Use the stored SoundPlayer instance
            player.luck -= 1
            print(f"You got lucky! Your luck is now {player.luck}")
            return "lucky!"
        else:
            self.sound_player.play_sound('unlucky.wav')  # Use the stored SoundPlayer instance
            player.luck -= 1
            print(f"You got unlucky! Your luck is now {player.luck}.")
            return "unlucky!"

    def roll_dice_battle(self, num_dice, skill):
        roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + skill
        return roll_total
    
    def conduct_battle(self):
        if self.monster:
            roll_luck = input("Do you want to use your luck during the battle? (Y/N): ").strip().lower()
            if roll_luck == 'y':
                roll_luck = True
            else:
                roll_luck = False

            while self.player.stamina > 0 and self.monster.stamina > 0:
                player_roll = self.roll_dice_battle(2, self.player.skill)
                monster_roll = self.roll_dice_battle(2, self.monster.skill)

                print(f"Player rolled {player_roll}. Monster rolled {monster_roll}.")

                if player_roll > monster_roll:
                    self.player_attacks(roll_luck)
                elif monster_roll > player_roll:
                    self.monster_attacks(roll_luck)
                else:
                    print("It's a tie!")

        else:
            print("Monster not found.")

    def player_attacks(self, roll_luck):
        print("Player wins!")
        self.sound_player.play_sound('heroattack.wav')
        self.apply_staminaLoss(self.monster, self.player, roll_luck)

    def monster_attacks(self, roll_luck):
        print("Monster wins!")
        self.sound_player.play_sound('orcattack.wav')
        self.apply_staminaLoss(self.player, self.monster, roll_luck)

    def apply_staminaLoss(self, attacker, defender, roll_luck):
        staminaLoss = -2
        if roll_luck:
            luck_result = self.roll_dice_luck(attacker)
            if "lucky" in luck_result:
                print(f"{attacker.name} got lucky! Damage increased.")
                staminaLoss -= 1
            else:
                print(f"{attacker.name} got unlucky! Damage decreased.")
                staminaLoss += 1

        defender.stamina += staminaLoss