from werkzeug.security import generate_password_hash, check_password_hash
from app.config import book_api2

class Helpers:

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    
    @staticmethod
    def get_book_api(query):
        return f"{book_api2}{query}"