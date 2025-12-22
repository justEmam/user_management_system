# models.py — Data Structure Definition

# Responsibilities:

# Define:

# User entity

#Admin (same)

# Activity log entity
class User:
        id:int
        username:str
        email:str
        role: str
        is_active:bool
        password_hash:str

class Admin(User):
        pass

class ActivityLog:
        id:int
        user_id:int #Foreign Key. 
        action:str
        timestamp:str


