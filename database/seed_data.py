import sqlite3

# Connect to the existing database
conn = sqlite3.connect("database/users.db")
cur = conn.cursor()

# Insert an admin user
cur.execute("""
INSERT INTO users (username, email, password_hash, role)
VALUES (?, ?, ?, ?)
""", ("admin", "admin@example.com", "hashed_password_here", "admin"))

# Optional: insert some demo users
demo_users = [
    ("user1", "user1@example.com", "hashed_password_here", "user"),
    ("user2", "user2@example.com", "hashed_password_here", "user")
]

cur.executemany("""
INSERT INTO users (username, email, password_hash, role)
VALUES (?, ?, ?, ?)
""", demo_users)

conn.commit()
conn.close()
