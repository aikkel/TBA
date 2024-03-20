from Maps.Rooms import Room

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.skills = {}
        self.stamina = 100
        self.luck = 10
        self.current_room = None  # Initialize current room as None

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


    def update_current_room(self, room):
        self.current_room = room

# Create a player instance
player = Player("Player 1")

# Set the initial current room to c1
player.update_current_room(Room.all_rooms[0])  # Assuming c1 is the first room in the list


# Move the player to next rooms
player.move("east")
player.move("west")
player.move("south")
player.move("east")