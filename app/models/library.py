"""
Library Model
"""

class Library:

    def __init__(self, id=None, name=None, description=None, logo_url=None, coordinates=None):
        self.id = id
        self.name = name
        self.description = description
        self.logo_url = logo_url
        self.coordinates = coordinates

class LibraryHours:

    def __init__(self, library_id=None, day_of_week=None, open_time=None, close_time=None):
        self.library_id = library_id
        self.day_of_week = day_of_week
        self.open_time = open_time
        self.close_time = close_time
