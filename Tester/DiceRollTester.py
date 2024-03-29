
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import random
# from Units.Player import Player
# # from Units.Monster import Monster
# # from Scenarios.DiceRoller import DiceRoller



# class DiceRoller:
#     def __init__(self, name):
#         self.player = Player(name)

#     def roll_dice_player(self, num_dice, modifier=0):
#         roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + modifier
#         return roll_total
    
#     def roll_dice_luck(self, player):
#         luck_roll = random.randint(2, 12)
#         if luck_roll <= player.luck:
#             player.luck -= 1
#             print(f"You got lucky! Your luck is now {player.luck}" )
#             return "lucky! " + str(player.luck)
#         else:
#             player.luck -= 1
#             return "unlucky!"


#     def roll_dice_battle(num_dice, skill):
#         roll_total = sum([random.randint(1, 6) for _ in range(num_dice)]) + skill
#         return roll_total
    
#     def conduct_battle(self, monster, roll_luck=False):
#         player_roll = self.roll_dice_battle(2, self.player.skill)
#         monster_roll = self.roll_dice_battle(2, monster.skill)

#         print(f"Player rolled {player_roll}. Monster rolled {monster_roll}.")

#         if player_roll > monster_roll:
#             print("Player wins!")
#             if roll_luck:
#                 luck_result = self.roll_dice_Luck(self.player)
#                 if "lucky" in luck_result:
#                     print("Player got lucky! Damage increased.")
#                 else:
#                     print("Player got unlucky! Damage decreased.")
#         elif monster_roll > player_roll:
#             print("Monster wins!")
#         else:
#             print("It's a tie!")


# def test_dice_roller():
#     # Create a DiceRoller instance
#     dice_roller = DiceRoller("Test Player")

#     # Test roll_dice_player
#     roll_player = dice_roller.roll_dice_player(3, 2)
#     assert 3 <= roll_player <= 20, f"Unexpected roll_dice_player result: {roll_player}"
#     print("Player roll: ", roll_player)

#     # Test roll_dice_luck
#     luck_result = dice_roller.roll_dice_luck(dice_roller.player)
#     assert luck_result in ["lucky!", "unlucky!"], f"Unexpected roll_dice_luck result: {luck_result}"

#     # Test roll_dice_battle
#     # roll_battle = dice_roller.roll_dice_battle(2, 5)
#     # assert 2 <= roll_battle <= 17, f"Unexpected roll_dice_battle result: {roll_battle}"
#     # skill and = 1d6+6, meaning pass 1,6
#     #stamina = 2d6+12, meaning pass 2,12


#     print("All tests passed!")
#     print("Luck = ", luck_result)

# test_dice_roller()