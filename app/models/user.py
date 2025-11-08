"""

User model

"""
from app.utils.helpers import Helpers

class User:
    
    def __init__(self, user_id=None, library_id=None, name=None, surname=None, 
                 email=None, phone=None, password=None, role=None, isactive=None):
        self.user_id = user_id
        self.library_id = library_id
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.password_hash = Helpers.hash_password(password)
        self.role = role
        self.isactive = isactive