from Maps.Rooms import all_rooms
# instead of having all these else statements, you could have a dictionary of roomID: function pairs
# also player input is repeated alot, you could make a function for that, to reduce code duplication
# food for thought when we start doing code extraction and refactoring

def GetInput(prompt):
    print(prompt)
    test = input().lower()
    if test == "y":
        return True
    elif test == "n":
        return False
    else:
        print("Invalid input. Please enter Y or N.")
        return GetInput(prompt)

def RunEvent(roomID):
    from Units.Player import Player
    from Scenarios.DiceRoller import DiceRoller
    # Create a Player instance with the DiceRoller instance
    player_instance = Player("Player 1")
    dice_roller = DiceRoller(None, None)
    if (roomID == 'r343'):
        print("A room. With a pit. The pit IS the room. You fall down the room pit and lose 1 Stamina. Now isn't that unfortunate.")
        player_instance.stamina -= 1
        print(f"Your Stamina is now {player_instance.stamina}.")
        all_rooms[2].remove_event('r343') # I think this works for removing an event from a room
        player_instance.update_current_room('2', all_rooms)


    elif (roomID == 'c278'):
        print("You see a locked door. It does not look very durable, you could attempt to bust it open with brute force...")
        prompt = "Attempt to force the door open? (Y/N)   "
        
        test = GetInput(prompt)

        if test:
            skillCheck = dice_roller.roll_dice_player(2)
            if skillCheck >= player_instance.skill:
                print("You smash your way through the door, dashing through the frame and enter...")
                all_rooms[1].remove_event('c278') # Delete event here
                # Here you'd be redirected to the next room, immediately starting r343's event
                player_instance.update_current_room('1', all_rooms) 
            else:
                print("Your strength wasn't enough to force open the door.")
                all_rooms[1].remove_event('c278') # Delete event here
        else:
            print("You decide against forcing the door open.")
            all_rooms[1].remove_event('c278') # Delete event here

    elif (roomID == 'c71'):
        print("You spot a sleeping orc. You must test your luck here to get through without waking it up...")
        luckCheck = dice_roller.roll_dice_luck(player_instance)
        if luckCheck == "lucky!":
            print("You pass by without waking the orc. It doesn't appear like it will wake anytime soon.")
            all_rooms[3].remove_event('c71')
            # player.update_current_room('', all_rooms) Don't know which room it is yet
        elif luckCheck == "unlucky!":
            print("The orc suddenly darts awake and eyes you aggressively!")
            # Run a battle here
            # Don't know how to handle battle stuff
            all_rooms[3].remove_event('c71')
        

    elif (roomID == 'r82'): # Room with box and sleeping orc
        print("You spot a box, being guarded quite poorly by a sleeping orc.")
        print("You could sneak past it and steal the box, but you would need some luck to do so.")
        prompt = "Attempt to steal the box? (Y/N)   "

        test = GetInput(prompt)

        if test:
            print("You dash towards the box and...")
            luckCheck = dice_roller.roll_dice_luck(player_instance)
            if luckCheck == "lucky!":
                print("...the orc snores loudly.")
                # No battle.
            if luckCheck == "unlucky!":
                print("...the orc wakes up!")
                # Initialize battle.
            print("You open the box and gain 1 GP.")
            # Add 1 GP to player inventory
            # Gain 2 Luck (can't go above initial luck)
            all_rooms[5].remove_event('r82')
        else:
            print("You decide to not risk waking this orc.")
            all_rooms[5].remove_event('r82')


    elif (roomID == 'r397'): # Room with monster-in-a-box
        print("You spot a box. Suspiciously enough, it is not being guarded.")
        print("There don't seem to be any traps nearby either.")
        prompt = "Open the box? (Y/N)  "

        test = GetInput(prompt)

        if test:
            print("A snake jumps from out of the box!")
            # Initialize battle

            print("With the snake slain, you check inside the box and loot a key. Engraved is the number 99.")
            # Add Key99 to player inventory
            # Gain 1 Luck (can't go above initial luck)
            all_rooms[7].remove_event('r397')
            
        else:
            print("This is clearly too good to be true. You walk away.")
            all_rooms[7].remove_event('r397')


    elif (roomID == 'r370'): # Room with two drunk orcs
        print("You enter the room and notice two drunk orcs guarding a box.")
        print("They don't seem to have spotted you, you could make your way back out if you wanted.")
        prompt = "Fight the orcs? (Y/N)  "

        test = GetInput(prompt)

        if test:
            # Initialize battle

            print("You approach the box and open it.")
            print("You see a tome. It has some cryptic spell inside... something about Dragon Fire...?")
            # I don't think the spell will be useful in this code specifically but eh
            all_rooms[9].remove_event('r370')
            
        else:
            print("They didn't even notice you on your way out.")
            all_rooms[9].remove_event('r370')


    else:
        print("DEBUG TEXT: There is no event here.")
        pass