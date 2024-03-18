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
            description += "\n\nYou can go" + ", ".join(self.exits) + "."
        if self.events:
            description += "\n\nEvents: " + ", ".join(self.events)
        return description

    def add_exit(self, direction, room):#modify to add multiple exits, use sublists
        self.exits[direction] = room

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
    
# Create rooms id, name, description, exits, items, events

c1 = Room('0', 'Cave Entrance', 'NEEDS DESCRIPTION.')
c278 = Room("1", "Corridor 1", "NEEDS DESCRIPTION.")
r343 = Room("2", "Pit", "NEEDS DESCRIPTION.")
c71 = Room("3", "Corridor 2", "NEEDS DESCRIPTION.")
c301 = Room("4", "Corridor 3", "NEEDS DESCRIPTION.")
r82 = Room("5", "NEED NAME", "NEEDS DESCRIPTION.")
c208 = Room("6", "Corridor 4", "NEEDS DESCRIPTION.")
r397 = Room("7", "NEED NAME", "NEEDS DESCRIPTION.")

# Add exits to rooms
# needs modification to add multiple exits
c1.add_exit("east", c278)
c1.add_exit("west", c71)
c278.add_exit("west", c1)
c278.add_exit("east", r343)
r343.add_exit("west", c278)


# When you call the add_exit method multiple times
# for the same direction, it will simply overwrite the previous
# exit with the new one. This means that only one exit will be stored per direction.
# If you need to have multiple exits in the same direction
# (e.g., a room with multiple doors to the north),
# you can store them as a list or a set within the exits dictionary. However,
# you would need to modify the add_exit method and adjust the logic accordingly to handle this scenario.



# Add items to rooms(items dont really exist yet)
r82.add_item("Key(99)") #key is an item not used in demo/prototype
r397.add_item("Spellbook") #Spellbook is an item not used in demo/prototype 

# Add events to rooms(events dont really exist yet)
c71.add_event("Pitfall!, you take -1 Stamina.")# need to add a function to remove stamina
