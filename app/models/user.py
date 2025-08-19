"""

User model

"""
from app.utils.helpers import Helpers

class User:
    
    def __init__(self, library_id, name, surname, email, phone, password, role):
        self.library_id = library_id
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.password_hash = Helpers.hash_password(password)
        self.role = role
        self.isactive = 1