class Room:
    def __init__(self, id, name, description, exits=None, items=None, event=None):
        self.id = id                                     # Room's ID, how it is called
        self.name = name                                 # Room Name
        self.description = description                   # Room's description
        self.exits = exits if exits is not None else {}  # Exit(s) from a room
        self.items = items if items is not None else []  # Item(s) found in a room
        self.event = event                               # Traps / teleport traps / enemies in a room
    
    def get_description(self):
        description = self.description
        if self.items:
            description += "\n\nYou see" + ", ".join((self.items)) + " here."
        if self.exits:
            description += "\n\nYou can go" + ", ".join(self.exits) + "."
        return description

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
    
# Create rooms id, name, description, exits, items, event

c1 = Room('0', 'Cave Entrance', 'NEEDS DESCRIPTION.', None, None, None)
c278 = Room("1", "Corridor 1", "NEEDS DESCRIPTION.", None, None, None)
r343 = Room("2", "Pit", "NEEDS DESCRIPTION.", None, None, None)
c71 = Room("3", "Corridor 2", "NEEDS DESCRIPTION.", None, None, None)
c301 = Room("4", "Corridor 3", "NEEDS DESCRIPTION.", None, None, None)
r82 = Room("5", "NEED NAME", "NEEDS DESCRIPTION.", None, None, None)
c208 = Room("6", "Corridor 4", "NEEDS DESCRIPTION.", None, None, None)
r397 = Room("7", "NEED NAME", "NEEDS DESCRIPTION.", None, None, None)

# Add exits to rooms
c1.add_exit("east", c278)
c1.add_exit("west", c71)
c278.add_exit("west", c1)
c278.add_exit("east", r343)
r343.add_exit("west", c278)

# Add items to rooms(items dont really exist yet)
r82.add_item("Key(99)") #key is an item not used in demo/prototype
r397.add_item("Spellbook") #Spellbook is an item not used in demo/prototype 

# Add events to rooms(events dont really exist yet)
c71.add_event("Pitfall!, you take -1 Stamina.")# need to add a function to remove stamina