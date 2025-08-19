"""
Library Model
"""

from app.services.library_service import LibraryManager

class Library:

    def __init__(self, name, description, logo_url):
        self.name = name
        self.description = description
        self.logo_url = logo_url