import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
from Media.Art import ArtReader

class Monster:
    def __init__(self, id, name, skill, stamina, art_reader):
        self.id = id
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.art_reader = art_reader

    def show_art(self):
        print(f"Art for Monster ID {self.id}:")
        if self.id in range(1, 5):
            self.art_reader.orc()
        elif self.id == 5:
            self.art_reader.snake()
        else:
            print("No art available for this monster.")

    @staticmethod
    def retrieve_monster_from_db(database_file, art_reader, monster_id):
        conn = sqlite3.connect(database_file)
        c = conn.cursor()

        # Retrieve data for the specified monster ID from the monsters table
        c.execute('SELECT * FROM monsters WHERE id=?', (monster_id,))
        monster_data = c.fetchone()

        # Close connection
        conn.close()

        if monster_data:
            return Monster(*monster_data, art_reader)
        else:
            return None


# Usage example
art_reader = ArtReader('Media/Art.txt')

# Retrieve monster with ID 1 from the database
monster = Monster.retrieve_monster_from_db('monsters.db', art_reader, None)

# If the monster exists, show its art
if monster:
    monster.show_art()
else:
    print("Monster not found.")
