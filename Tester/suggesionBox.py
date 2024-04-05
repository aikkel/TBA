# def get_player_input(prompt):
#     print(prompt)
#     test = input().lower()
#     if test == "y":
#         return True
#     elif test == "n":
#         return False
#     else:
#         print("Invalid input. Please enter Y or N.")
#         return get_player_input(prompt)
    
#     elif (roomID == 'c278'):
#         print("You see a locked door. It does not look very durable, you could attempt to bust it open with brute force...")
#         if get_player_input("Attempt to force the door open? (Y/N)"):
#             skillCheck = dice_roller.roll_dice_player(2)
#             if skillCheck >= player_instance.skill:
#                 print("You smash your way through the door, dashing through the frame and enter...")
#             else:
#                 print("Your strength wasn't enough to force open the door.")
#         else:
#             print("You decide against forcing the door open.")
#         all_rooms[1].remove_event('c278') # Delete event here