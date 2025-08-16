"""
Book and/or Library resources
"""

class Books:

    def __init__(self, library_id, title, isbn, category, total_copies, available_copies):
        self.library_id = library_id
        self.title = title
        self.isbn = isbn
        self.category = category
        self.total_copies = total_copies
        self.available_copies = available_copies

    def add(self):
        pass

    def edit(self):
        pass

    def delete_availability(self):
        pass