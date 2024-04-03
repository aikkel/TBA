from Maps.Rooms import *

from Scenarios.DiceRoller import DiceRoller

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.dice_roller = DiceRoller(name, sound_player=None)  # Pass player's name to DiceRoller
        self.skill = self.dice_roller.roll_dice_player(1, 6)
        self.stamina = self.dice_roller.roll_dice_player(2, 12)
        self.luck = self.dice_roller.roll_dice_player(1, 6)
        self.current_room = None  # Initialize current room as None

    def set_stats(self, skill, stamina, luck):
        self.skill = skill
        self.stamina = stamina
        self.luck = luck

    def move(self, direction):
        from Scenarios.EventHandler import RunEvent

        if self.current_room and direction in self.current_room.exits:
            next_rooms = self.current_room.exits[direction]
            if len(next_rooms) == 1:
                next_room = next_rooms[0]
                self.current_room = next_room
                print("You move to", self.current_room.name)
                if self.current_room.events:
                    RunEvent(self.current_room.events[0])

            elif len(next_rooms) > 1:
                print("There are multiple rooms in that direction. Please specify:")
                for i, room in enumerate(next_rooms):
                    print(f"{i+1}. {room.name}")
                while True:
                    choice = input("Enter the number of the room you want to move to: ")
                    try:
                        choice_index = int(choice) - 1
                        if 0 <= choice_index < len(next_rooms):
                            next_room = next_rooms[choice_index]
                            self.current_room = next_room
                            print("You move to", self.current_room.name)
                            break  # Exit the loop after successfully moving
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Invalid choice.")
        else:
            print("You can't go that way.")


    # Update the current room of the player, can be used in event handling
    def update_current_room(self, room_id):
        from Maps.Rooms import all_rooms
        #global all_rooms  # Access the global variable
        for room in all_rooms:
            if room.id == room_id:
                self.current_room = room
                break
        else:
            print(f"Room with ID {room_id} not found.")

