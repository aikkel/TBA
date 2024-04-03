import json
from Units.Player import Player

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        # Initialize the player
        self.player = None

    def encounter_monster(self):
        # (Simulate the battle or other relevant actions)
        # Update the player's level based on the battle result
        pass

    def save_game(self, filename="save.json"):
        if self.player is not None:
            if self.player.current_room:
                current_room_id = self.player.current_room.id
            else:
                current_room_id = None

            save_data = {
                "player": {
                    "name": self.player.name,
                    "inventory": self.player.inventory,
                    "skill": self.player.skill,
                    "stamina": self.player.stamina,
                    "luck": self.player.luck,
                    "current_room_id": current_room_id  # Include the current room ID
                },
            }

            with open(filename, "w") as file:
                json.dump(save_data, file, indent=4)
            print("Game saved successfully!")
        else:
            print("Error: No player instance.")

    def load_game(self, all_rooms, filename="save.json"):
        try:
            with open(filename, "r") as file:
                save_data = json.load(file)

            player_data = save_data["player"]
            self.player = Player(player_data["name"])
            self.player.inventory = player_data["inventory"]
            self.player.skill = player_data["skill"]
            self.player.stamina = player_data["stamina"]
            self.player.luck = player_data["luck"]

            # Load the current room if available
            current_room_id = player_data.get("current_room_id")
            if current_room_id:
                for room in all_rooms:
                    if room.id == current_room_id:
                        self.player.current_room = room
                        break
                else:
                    print(f"Error: Current room with ID {current_room_id} not found.")

            print("Game loaded successfully!")
        except FileNotFoundError:
            print("No save file found.")
        except json.JSONDecodeError:
            print("Error decoding the save file.")

    def RunGame(self, player, all_rooms):
        self.player = player
        # Loop through the game until the player quits or exits
        while True:
            current_room = self.player.current_room  # Get the current room from the player

            # Check if the current room is valid
            if current_room is None:
                print("Error: Player is not in any room.")
                break

            # Print the current room description
            print(current_room.get_description())

            # Get user input for direction or other actions
            action = input("Enter your action (direction or command): ").strip().lower()

            if action == "quit":
                print("Goodbye!")
                break
            elif action == "save":
                self.save_game()  # Save the game
            elif action == "load":
                self.load_game(all_rooms)  # Load the game
            elif action in current_room.exits:
                self.player.move(action)  # Move the player to the specified direction
            else:
                print("Invalid action. Please enter a valid direction, 'save', 'load', or 'quit'.")
