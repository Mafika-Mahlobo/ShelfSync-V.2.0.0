"""
Library Model
"""

from app.services.library_service import LibraryManager

class Library:

    def __init__(self, id, name, description, logo_url, coordinates):
        self.id = id
        self.name = name
        self.description = description
        self.logo_url = logo_url
        self.coordinates = coordinates
