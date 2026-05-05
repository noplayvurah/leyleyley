import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret')")
cursor.execute("INSERT INTO users (username, password) VALUES ('guest', 'guestpass')")
conn.commit()
conn.close()
print('database.db created with sample users')
