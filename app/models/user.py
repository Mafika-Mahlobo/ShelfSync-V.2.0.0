"""

User model

"""
from app.services.user_service import UserManager
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
        self.isactive = True

    def add(self):
        response = UserManager.save_to_db(( 
            self.library_id,
            self.name, 
            self.surname, 
            self.email, 
            self.phone, 
            self.password_hash,
            self.role,
              ))
        
        if(response):
            return f"{self.name} {self.surname} Has been successfully registered!"
        return "Error"
    
class Patron(User):
    pass

class Admin(User):
    pass

class GlobalAdmin(User):
    pass