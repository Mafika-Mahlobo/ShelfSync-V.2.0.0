"""
Library Model
"""

from app.services.library_service import LibraryManager

class Library:

    def __init__(self, name, description, logo_url):
        self.name = name
        self.description = description
        self.logo_url = logo_url

    def add(self):
        library_object = LibraryManager((self.name, self.description, self.logo_url))
        response = library_object.add_library() 
        return response["message"]

    def delete(self):
        library_object = LibraryManager((self.name, self.description, self.logo_url))
        response = library_object.delete_library()
        return response["message"]

    def edit(self):
        pass