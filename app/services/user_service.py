""""
User service Test

"""

from app.models.user import User

class Patron:

    def __init__(self, name):
        self.name = name

    def create_user(self):
        person = User(self.name)
        return f"Hello {person.name}"

    