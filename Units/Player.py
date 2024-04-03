from Maps.Rooms import *
from Maps.Rooms import all_rooms
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
        if self.current_room and direction in self.current_room.exits:
            next_rooms = self.current_room.exits[direction]
            if len(next_rooms) == 1:
                next_room = next_rooms[0]
                self.current_room = next_room
                print("You move to", self.current_room.name)
            elif len(next_rooms) > 1:
                print("There are multiple rooms in that direction. Please specify:")
                for i, room in enumerate(next_rooms):
                    print(f"{i+1}. {room.name}")
                choice = input("Enter the number of the room you want to move to: ")
                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(next_rooms):
                        next_room = next_rooms[choice_index]
                        self.current_room = next_room
                        print("You move to", self.current_room.name)
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid choice.")
        else:
            print("You can't go that way.")



    # Update the current room of the player, can be used in event handling
    def update_current_room(self, room_id, all_rooms):
        for room in all_rooms:
            if room.id == room_id:
                self.current_room = room
                break
        else:
            print(f"Room with ID {room_id} not found.")

    def get_description(self):
        description = self.description
        if self.items:
            description += "\n\nYou see " + ", ".join(self.items) + " here."
        if self.exits:
            exit_descriptions = []
            for direction, rooms in self.exits.items():
                room_names = [room.name for room in rooms]
                exit_descriptions.append(f"{direction}: {', '.join(room_names)}")
            description += "\n\nYou can go " + ", ".join(exit_descriptions) + "."
        if self.events:
            description += "\n\nEvents: " + ", ".join(self.events)
        return description


# Create a player instance
player = Player("Player 1")

# Sets the initial current room to c1
player.update_current_room('0', all_rooms)

# Move the player to next rooms
player.move("east")
player.move("west")
player.move("south")
player.move("east")