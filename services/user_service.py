import re
import sqlite3
import bcrypt
from database.models import User,Admin
# user_service.py — User Operations

# Responsibilities:

# Create user

# Update user

# Delete / deactivate user

# Fetch users (search, filter)

# Rules:
# ❌ No UI widgets
# ❌ No SQL strings inside UI
# ✅ Business rules live here

class UserService:
    @staticmethod
    def validateUserName(user_name:str) -> bool:
        #checks on username: unique and length > 4
        if len(user_name)<4:
            raise ValueError("Username should have more than 4 characters")
        
        conn = sqlite3.connect('database/users.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT 1 from users WHERE username = ?""",(user_name,))
        availableuser = cursor.fetchone()
        if availableuser:
            raise ValueError("This username is taken")
        conn.close()
        return True
    
    @staticmethod
    def validateEmail(email:str) -> bool:
        #checks on email, default email pattern
        EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match (EMAIL_REGEX,email) is None:
            raise ValueError("Please enter a valid email")
        else:
            return True
        
    
    @staticmethod
    def validatepw(password:str) -> bool: #basic pw checking
        if len(password) >= 6:
            return True
        else:
            raise ValueError("Password must be longer than or equal to 6 chars")

    @staticmethod
    def createUser(user_name,email,password)-> User:
        if UserService.validateUserName(user_name) and UserService.validateEmail(email) and UserService.validatepw(password):
            user = User()
            user.username=user_name
            user.email = email
            user.role = "user"
            user.is_active=True
            hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
            hashed_password = hashed.decode()
            user.password_hash = hashed_password

            conn = sqlite3.connect('database/users.db')
            cursor = conn.cursor()
            cursor.execute("""
                           INSERT INTO users (username, email, password_hash, role)
                           values (?,?,?,?)""", (user.username,user.email,user.password_hash,user.role) )
            
            conn.commit()
            conn.close()

#Stop now
#To do -> User can change only his password (1)
#Users can search users by username, just like in forums. (2)
#Admin can delete users, and change password of any user(3), and deactivate any user.(4)


