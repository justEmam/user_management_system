import bcrypt
import sqlite3
from database.models import User
# auth_service.py — Authentication & Authorization

# Responsibilities:

# Login validation

# Password hashing

# Role checking (admin / viewer)

# Session state handling

# Rules:
# ❌ No UI
# ❌ No DB table creation
# ✅ Security logic only


class AuthService:

    @staticmethod
    def login(username: str, password: str) -> User:
        conn = sqlite3.connect('database/users.db')
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, username, email, password_hash, role, is_active
            FROM users
            WHERE username = ? AND is_active = 1
            """,
            (username,)
        )
        row = cursor.fetchone()
        conn.close()

        if row is None:
            raise ValueError("Wrong username or password")

        user_id, username, email, password_hash, role, is_active = row

        if not bcrypt.checkpw(password.encode(), password_hash.encode()):
            raise ValueError("Wrong username or password")

        user = User()
        user.id = user_id
        user.username = username
        user.email = email
        user.password_hash = password_hash
        user.role = role
        user.is_active = bool(is_active)

        return user

class Session:
    current_user: User | None = None

        

        


