"""
Book and/or Library resources
"""

class Books:

    def __init__(self, library_id, title, description, image_link, isbn, authors, category, total_copies, available_copies):
        self.library_id = library_id
        self.title = title
        self.description = description
        self.image_link = image_link
        self.isbn = isbn
        self.authors = authors
        self.category = category
        self.total_copies = total_copies
        self.available_copies = available_copies