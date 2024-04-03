# all_rooms = [] # Initialize the list to store all rooms

class Room:
    
    def __init__(self, id, name, description, exits=None, items=None, events=None):
        self.id = id                                        # Room's ID, how it is called
        self.name = name                                    # Room Name
        self.description = description                      # Room's description
        self.exits = exits if exits is not None else {}     # Exit(s) from a room
        self.items = items if items is not None else []     # Item(s) found in a room
        self.events = events if events is not None else []  # Events in a room


    def get_description(self):
        description = self.description
        if self.items:
            description += "\n\nYou see" + ", ".join((self.items)) + " here."
        if self.exits:
            exit_descriptions = []
        for direction, rooms in self.exits.items():
            room_names = [room.name for room in rooms]
            exit_descriptions.append(f"{direction}: {', '.join(room_names)}")
            description += "\n\nYou can go " + ", ".join(exit_descriptions) + "."
        if self.events:
            description += "\n\nEvents: " + ", ".join(self.events)
        return description

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
    
    def add_event(self, event):
        self.events.append(event)
    
    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)
            return event
    
    def add_exit(self, direction, room):
        if direction in self.exits:
            self.exits[direction].append(room)
        else:
            self.exits[direction] = [room]

all_rooms = [] # Initialize the list to store all rooms  
# Create rooms id, name, description, exits, items, events
c1 = Room("0", "Cave Entrance", "NEEDS DESCRIPTION.")
c278 = Room("1", "Corridor 1", "NEEDS DESCRIPTION.")
r343 = Room("2", "Pit", "NEEDS DESCRIPTION.") # pit should not be called pit probably
c71 = Room("3", "Corridor 2", "NEEDS DESCRIPTION.")
c301 = Room("4", "Corridor 3", "NEEDS DESCRIPTION.")
r82 = Room("5", "NEED NAME", "NEEDS DESCRIPTION.")
c208 = Room("6", "Corridor 4", "NEEDS DESCRIPTION.")
r397 = Room("7", "NEED NAME", "NEEDS DESCRIPTION.")
c363 = Room("8", "Corridor 5", "NEEDS DESCRIPTION.")
r370 = Room("9", "NEED NAME", "NEEDS DESCRIPTION.")

# Add rooms to the list
all_rooms.extend([c1, c278, r343, c71, c301, r82, c208, r397, c363, r370])

# Add exits to rooms
# east west corridor
c1.add_exit("east", c278)
c1.add_exit("west", c71)

c278.add_exit("west", c1)
c278.add_exit("east", r343)

r343.add_exit("west", c278)




# Add items to rooms(items dont really exist yet)
r82.add_item("box?") #box is an item containing item 1gold and a mouse that runs away +2 luck points
r397.add_item("another box")# contain a snake, to battle
r370.add_item("and another box")#in box is a Spellbook, used in demo/prototype, called how to cast dragon fire


# Add events to rooms(events dont really exist yet)
r343.add_event('r343')# need to add a function to remove stamina
c278.add_event('c278')# need to add a function to unlock door
c71.add_event("sneak past the sleeping orc, roll luck")# need to add a function to sneak past orc
r82.add_event("sleeping orc, roll luck to sneak past, or fight")# need to add a function to sneak past orc
r397.add_event("snake in the box, if opeen box, battle initiate")# need to add a function to trigger battle. if won get +1 luck
r370.add_event("drunken monsters!? 2x orc")# need to add a function to trigger battle or run away. drunken state allow +1 to rolls
