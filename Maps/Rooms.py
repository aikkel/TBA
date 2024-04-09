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
c1 = Room("0", "Cave Entrance", "You peer into the gloom to see dark, slimy walls with pools of water on the stone floor in front of you. The air is cold and dank.")
c278 = Room("1", "Corridor(1)", "The passageway soon comes to an end at a blocked wooden door. You listen to the door but hear nothing.")
r343 = Room("2", "Locked door", "The door bursts open and you fall headlong into a room. But your heart jumps as you realize you are not landing on the floor, but plunging down a pit!")
c71 = Room("3", "Corridor(2)", "You can see a strange Goblin-like creature in leather armour asleep at his post. You try to tiptoe past him. Test your luck.")
c301 = Room("4", "Corridor(3)", "There is a rough-cut wooden door. You can hear a rasping sound which may be some sort of creature snoring. Do you want to open the door?")
r82 = Room("5", "Room with a rasping noice", "Asleep is the same sort of creature that you found at the sentry post. You may creep into the room and try to take the box. Do you wanna test your luck?")
c208 = Room("6", "Corridor(4)", "Further up the passage along the west wall you see another door. You listen at it but hear nothing. Do you want to try open the door?")
r397 = Room("7", "Silent room", "The door opens.. There is a stale smell in the air. Under the table is a small box. Do you want to open the box?")
c363 = Room("8", "Corridor(5)", "Further up the passage on the west wall you see another similar door. You listen at the door and hear the worst singing! Do you want to go into the room?")
r370 = Room("9", "Loud room", "The door opens. A small box rests under the table. Around the table are two creatures. They are drinking. You assume they are drunk. Do you wanna fight?")

# Add rooms to the list
all_rooms.extend([c1, c278, r343, c71, c301, r82, c208, r397, c363, r370])

# Add exits to rooms
# east west corridor
c1.add_exit("east", c278)
c1.add_exit("west", c71)

c71.add_exit("east", c1)
c71.add_exit("north", c301)

c278.add_exit("west", c1)
# c278.add_exit("east", r343)

r343.add_exit("west", c278)

c301.add_exit("south", c71)
c301.add_exit("west", r82)
c301.add_exit("north", c208)

r82.add_exit("east", c301)

c208.add_exit("south", c301)
c208.add_exit("west", r397)
c208.add_exit("north", c363)

r397.add_exit("east", c208)

c363.add_exit("south", c208)
c363.add_exit("west", r370)


# Add items to rooms(items dont really exist yet)
c1.add_item("Potion of Skill/Strength/Fortune") # At the start of the game, you can choose between one of three potions
r82.add_item("box?")                            # box is an item containing item 1gold and a mouse that runs away +2 luck points
r397.add_item("another box")                    # contain a snake, to battle
r370.add_item("and another box")                #in box is a Spellbook, used in demo/prototype, called how to cast dragon fire

# Add events to rooms
# Please do not change the event names, they are used for EventHandler.py

r343.add_event("r343")  # need to add a function to remove stamina
c278.add_event("c278")  # need to add a function to unlock door
c71.add_event("c71")    # need to add a function to sneak past orc
r82.add_event("r82")    # need to add a function to sneak past orc
r397.add_event("r397")  # need to add a function to trigger battle. if won get +1 luck
r370.add_event("r370")  # need to add a function to trigger battle or run away. drunken state allow +1 to rolls