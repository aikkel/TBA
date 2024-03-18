import random
from Units import Player

class DiceRoller:
    def __init__(self, name):
        self.player = Player(name)

    def roll_dice_Player(num_dice, modifier=0):
        roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + modifier
        return roll_total
    
    #Rolling dice for luck scenarios.
    def roll_dice_Luck(player):
        luck_roll = random.randint(2, 12)
        if luck_roll <= player.luck:
            player.luck -= 1 #decrease luck by 1
            print(f"You got lucky! Your luck is now {player.luck}" )
            return "lucky!" + player.luck
        else:
            player.luck -= 1 #decrease luck by 1
            return "unlucky!"


    def roll_dice_Battle(num_dice, skill):
        roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + skill #dont forget luck
        return roll_total