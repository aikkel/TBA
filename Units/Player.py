from Maps.Rooms import *
from Maps.Rooms import all_rooms
from Scenarios.DiceRoller import DiceRoller

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.dice_roller = DiceRoller(name)  # Pass player's name to DiceRoller
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
            next_room = self.current_room.exits[direction]
            if isinstance(next_room, list):  # Check if the exit leads to multiple rooms
                print("There are multiple rooms in that direction. Please specify.")
                return
            self.current_room = next_room
            print("You move to", self.current_room.name)
        else:
            print("You can't go that way.")

    # Update the current room of the player, can be used in event handling
    def update_current_room(self, room_id):
        for room in all_rooms:
            if room.id == room_id:
                self.current_room = room
                break
        else:
            print(f"Room with ID {room_id} not found.")

# Create a player instance
player = Player("Player 1")
        
# Sets the initial current room to c1
player.update_current_room('0')

# Move the player to next rooms
player.move("east")
player.move("west")
player.move("south")
player.move("east")