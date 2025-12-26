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
    validateLogin(username:str,pass:str):
    