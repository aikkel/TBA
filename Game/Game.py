import json
import threading
from Units.Player import Player
from Scenarios.DiceRoller import DiceRoller
from Scenarios.EventHandler import RunEvent
from Media.Art import ArtReader


class Game:
    def __init__(self, sound_player, sound_lock):
        self.sound_player = sound_player
        self.sound_lock = sound_lock  # Store the sound lock
        
        self.dice_roller = DiceRoller("Dice Roller", self.sound_player)
        self.initialize_game()

    def initialize_game(self):
        self.player = None

    def encounter_monster(self):
        pass

    def show_title(self):
        art_reading = ArtReader('Media/Art.txt')
        art_reading.titel()

    def save_game(self, filename="save.json"):
        try:
            with self.player_lock:  # Acquire lock before accessing/modifying player data
                if self.player:
                    current_room_id = self.player.current_room.id if self.player.current_room else None
                    save_data = {
                        "player": {
                            "name": self.player.name,
                            "inventory": self.player.inventory,
                            "skill": self.player.skill,
                            "stamina": self.player.stamina,
                            "luck": self.player.luck,
                            "current_room_id": current_room_id
                        },
                    }

                    with open(filename, "w") as file:
                        json.dump(save_data, file, indent=4)
                    print("Game saved successfully!")
                else:
                    print("Error: No player instance.")
        finally:
            self.player_lock.release()  # Release lock after operation is complete

    def load_game(self, all_rooms, filename="save.json"):
        try:
            with self.player_lock:  # Acquire lock before accessing/modifying player data
                with open(filename, "r") as file:
                    save_data = json.load(file)

                    player_data = save_data.get("player")
                    if player_data:
                        self.player = Player(player_data["name"])
                        self.player.inventory = player_data["inventory"]
                        self.player.skill = player_data["skill"]
                        self.player.stamina = player_data["stamina"]
                        self.player.luck = player_data["luck"]

                        current_room_id = player_data.get("current_room_id")
                        if current_room_id:
                            for room in all_rooms:
                                if room.id == current_room_id:
                                    self.player.current_room = room
                                    break
                        else:
                            print(f"Error: Current room with ID {current_room_id} not found.")
                    else:
                        print("Error: No player data found.")

                print("Game loaded successfully!")
        except FileNotFoundError:
            print("No save file found.")
        except json.JSONDecodeError:
            print("Error decoding the save file.")

    def RunGame(self, player, all_rooms):
        self.player = player
        self.show_title()

        while True:
            current_room = self.player.current_room

            if not current_room:
                print("Error: Player is not in any room.")
                break

            # description_lines = current_room.get_description().split('\n\n')
            # room_description = description_lines[0]
            # possible_exits = [line[len("You can go "):].split(", ") for line in description_lines[1:] if line.startswith("You can go ")][0] if description_lines[1:] else []

            description_lines = current_room.get_description().split('\n\n')
            room_description = description_lines[0]
            possible_exits = []
            for line in description_lines[1:]:
                if line.startswith("You can go "):
                    possible_exits = line[len("You can go "):].split(", ")
                    break

            print(room_description)
            if possible_exits:
                print("Possible exits: ", ", ".join(possible_exits))

            action = input("Enter your action (direction or command): ").strip().lower()

            if action == "quit":
                print("Goodbye!")
                break
            elif action == "save":
                self.save_game()
            elif action == "load":
                self.load_game(all_rooms)
            elif action in current_room.exits:
                self.player.move(action)
                if self.player.current_room.events:
                    RunEvent(self.player.current_room.events[0], self.dice_roller, self.player)
                else:
                    print("There are no events in this room.")
            else:
                print(f"Invalid action. Please enter a valid direction {', '.join(current_room.exits.keys())}, 'save', 'load', or 'quit'.")


