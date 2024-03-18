from Maps import Rooms as room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.inventory = []
        self.skills = {}
        self.stamina = 100
        self.luck = 10
        self.name = name
        self.current_room = current_room  # Store the current room ID

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print("You move to", self.current_room.name)
        else:
            print("You can't go that way.")

# Create a player
player = Player("Player 1", room)

# Move the player to next room
player.move("north")
player.move("west")
player.move("south")
player.move("east")
