import sqlite3

conn = sqlite3.connect('monsters.db')
c = conn.cursor()

c.execute('''CREATE TABLE monsters
             (id INTEGER PRIMARY KEY,
             name TEXT,
             skill INTEGER,
             stamina INTEGER)''')

monsters_data = [
    ("Goblin", 6, 10),
    ("Orc", 8, 15),
    ("Skeleton", 5, 8),
    # You can add more monsters here
]

c.executemany('INSERT INTO monsters (name, skill, stamina) VALUES (?, ?, ?)', monsters_data)

# Commit changes and close connection
conn.commit()
conn.close()