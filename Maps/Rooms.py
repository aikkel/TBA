class Room:
    def __init__(self, id, name, description, exits, items, event):
        self.id = id                   # Room's ID, how it is called
        self.name = name               # Room Name
        self.description = description # Room's description
        self.exits = exits             # Exit(s) from a room
        self.items = items             # Item(s) found in a room
        self.event = event             # Traps / teleport traps / enemies in a room

    
    def get_description(self):
        description = self.description
        if self.items:
            description += "\n\nYou see" + ", ".join((self.items)) + " here."
        if self.exits:
            description += "\n\nYou can go" + ", ".join(self.exits) + "."
        return self.description

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
    
    def add_event(self, event):
        self.event = event
    
    def remove_event(self, event):
        if event == self.event:
            self.event = None
            return event
    

kitchen = Room("Kitchen", "You are in a dimly lit kitchen. There is a table in the center.")
living_room = Room("Living Room", "You enter a spacious living room with a cozy fireplace.")

kitchen.add_exit("north", living_room)
living_room.add_exit("south", kitchen)

kitchen.add_item("knife")
kitchen.add_item("apple")