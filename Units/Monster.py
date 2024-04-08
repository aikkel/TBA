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

    
    def retrieve_monsters_from_db(database_file, art_reader):
        conn = sqlite3.connect(database_file)
        c = conn.cursor()

        # Retrieve data from the monsters table
        c.execute('SELECT * FROM monsters')
        monsters_data = c.fetchall()

        # Close connection
        conn.close()
        
        monsters = {}
        for monster_data in monsters_data:
            monster = Monster(*monster_data, art_reader)
            monsters[monster.id] = monster

        return monsters
# Usage example
art_reader = ArtReader('Media/Art.txt')

# Retrieve monsters from the database
monsters = Monster.retrieve_monsters_from_db('monsters.db', art_reader)

# Accessing individual monsters by ID
monster_id = 1
monster = monsters.get(monster_id)
if monster:
    monster.show_art()
else:
    print(f"Monster with ID {monster_id} not found.")