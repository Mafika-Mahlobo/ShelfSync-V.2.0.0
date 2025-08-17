"""
Library Model
"""

class Library:

    def __init__(self, name, description, logo_url):
        self.name = name
        self.description = description
        self.logo_url = logo_url

    def add(self):
        return f"Library added! {self.name} Welcome to ShelfSync."

    def delete(self):
        pass

    def edit(self):
        pass