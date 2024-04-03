from Maps.Rooms import all_rooms


def RunEvent(roomID):
    from Units.Player import Player
    from Scenarios.DiceRoller import DiceRoller
    # Create a Player instance with the DiceRoller instance
    player_instance = Player("Player 1")

    if (roomID == 'r343'):
        print("A room. With a pit. The pit IS the room. You fall down the room pit and lose 1 Stamina. Now isn't that unfortunate.")
        player_instance.stamina -= 1
        print(f"Your Stamina is now {player_instance.stamina}.")
        all_rooms.index('r343').remove_event('r343') # I think this works for removing an event from a room


    if (roomID == 'c278'):
        print("You see a locked door. It does not look very durable, you could attempt to bust it open with brute force...")
        print("Attempt to force the door open? (Y/N)   ")
        
        test = input() # Input here

        if test == "Y" or test == "y":
            skillCheck = DiceRoller().roll_dice_player(2)
            if skillCheck >= player_instance.skills:
                print("You smash your way through the door, dashing through the frame and enter...")
                all_rooms.index('c278').remove_event('c278') # Important to delete this event once it's done, we don't want it to start again
                player_instance.update_current_room('2', all_rooms) # Here you'd be redirected to the next room, immediately starting r343's event
            else:
                print("Your strength wasn't enough to force open the door.")
                all_rooms.index('c278').remove_event('c278') # Delete event here
        elif test == "N" or test == "n":
            print("You decide against forcing the door open.")
            all_rooms.index('c278').remove_event('c278') # Delete event here
        else:
            pass # Invalid input handler?

        if (roomID == 'c71'):
            print("You spot a sleeping orc. You must test your luck here to get through without waking it up...")
            luckCheck = DiceRoller().roll_dice_luck(player_instance)
            if luckCheck == "lucky!":
                print("You pass by without waking the orc. It doesn't appear like it will wake anytime soon.")
                all_rooms.index('c71').remove_event('c71')
                # player.update_current_room('', all_rooms) Don't know which room it is yet
            elif luckCheck == "unlucky!":
                print("The orc suddenly darts awake and eyes you aggressively!")
                # Run a battle here
                # Don't know how to handle battle stuff
        

        if (roomID == 'r82'): # Room with box and sleeping orc
            print("You spot a box, being guarded quite poorly by a sleeping orc.")
            print("You could sneak past it and steal the box, but you would need some luck to do so.")
            print("Attempt to steal the box? (Y/N)  ")

            test = input() # Input here

            if test == "Y" or test == "y":
                print("You dash towards the box and...")
                luckCheck = DiceRoller().roll_dice_luck(player_instance)
                if luckCheck == "lucky!":
                    print("...the orc snores loudly.")
                    # No battle.
                if luckCheck == "unlucky!":
                    print("...the orc wakes up!")
                    # Initialize battle.
                print("You open the box and gain 1 GP.")
                # Add 1 GP to player inventory
                # Gain 2 Luck (can't go above initial luck)
                # Delete event
            
            elif test == "N" or test == "n":
                print("You decide to not risk waking this orc.")
                # Delete event
            
            else:
                pass # Invalid input handler


        if (roomID == 'r397'): # Room with monster-in-a-box
            print("You spot a box. Suspiciously enough, it is not being guarded.")
            print("There don't seem to be any traps nearby either.")
            print("Open the box? (Y/N)  ")

            test = input() # Input here

            if test == "Y" or test == "y":
                print("A snake jumps from out of the box!")
                # Initialize battle

                print("With the snake slain, you check inside the box and loot a key with the number 99.")
                # Add Key99 to player inventory
                # Gain 1 Luck (can't go above initial luck)
                # Delete event
            
            elif test == "N" or test == "n":
                print("This is clearly too good to be true. You walk away.")
                # Delete event
            
            else:
                pass # Invalid input handler


        if (roomID == 'r370'): # Room with two drunk orcs
            print("You enter the room and notice two drunk orcs guarding a box.")
            print("They don't seem to have spotted you, you could make your way back out if you wanted.")
            print("Fight the orcs? (Y/N)  ")

            test = input() # Input here

            if test == "Y" or test == "y":
                # Initialize battle

                print("You approach the box and open it.")
                print("You see a tome. It has some cryptic spell inside... something about Dragon Fire...?")
                # I don't think the spell will be useful in this code specifically but eh
                # Delete event
            
            elif test == "N" or test == "n":
                print("They didn't even notice you on your way out.")
                # Delete event
            
            else:
                pass # Invalid input handler


        else:
            print("DEBUG TEXT: There is no event here.")
            pass