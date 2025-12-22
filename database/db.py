import sqlite3

# Connect (creates users.db if it doesn't exist)
conn = sqlite3.connect("database/users.db")
cur = conn.cursor()

# Create users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active INTEGER DEFAULT 1
)
""")

conn.commit()
conn.close()
