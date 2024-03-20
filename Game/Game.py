import json
from Units.Player import Player


class Game:
    def __init__(self):
        self.player = Player("Player")

    def encounter_monster(self):
        # (Simulate the battle or other relevant actions)
        # Update the player's level based on the battle result
        self.player.stamina -= 10

    def save_game(self, filename="save.json"):
        save_data = {
            "player": {
                "name": self.player.name,
                "inventory": self.player.inventory,
                "skills": self.player.skills,
                "stamina": self.player.stamina,
                "luck": self.player.luck
            },
        }

        with open(filename, "w") as file:
            json.dump(save_data, file, indent=4)

    def load_game(self, filename="save.json"):
        try:
            with open(filename, "r") as file:
                save_data = json.load(file)

            player_data = save_data["player"]
            self.player = Player(player_data["name"])
            self.player.inventory = player_data["inventory"]
            self.player.skills = player_data["skills"]
            self.player.stamina = player_data["stamina"]
            self.player.luck = player_data["luck"]

            print("Game loaded successfully!")
        except FileNotFoundError:
            print("No save file found.")
        except json.JSONDecodeError:
            print("Error decoding the save file.")

# Create a game
game_instance = Game()

# Save the game
game_instance.save_game()

# Load the game
game_instance.load_game()
