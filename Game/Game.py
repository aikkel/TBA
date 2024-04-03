import json
from Units.Player import Player
from Maps.Rooms import all_rooms

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        # Initialize the player
        self.player = Player("Player")

    def encounter_monster(self):
        # (Simulate the battle or other relevant actions)
        # Update the player's level based on the battle result
        self.player.stamina -= 10

    def save_game(self, filename="save.json"):
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


    def RunGame():
        # Create a player instance
        player = Player("Player 1")
        player.update_current_room('0', all_rooms)  # Sets the initial current room to c1

        # Loop through the game until the player quits or exits
        while True:
            current_room = player.current_room  # Get the current room from the player

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
            elif action in current_room.exits:
                player.move(action)  # Move the player to the specified direction
            else:
                print("Invalid action. Please enter a valid direction or command.")

    # Call the RunGame function to start the game
    RunGame()



# Call the RunGame function to start the game
    RunGame()

# Create a game
game_instance = Game()

# Save the game
game_instance.save_game()

# Load the game
game_instance.load_game(all_rooms)