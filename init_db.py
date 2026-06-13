import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    profile_picture TEXT DEFAULT 'https://static.thenounproject.com/png/5100711-200.png'
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")