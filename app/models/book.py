"""
Book and/or Library resources
"""

class Books:

    def __init__(self, library_id=None, title=None, description=None, image_link=None, 
                 isbn=None, authors=None, category=None, total_copies=None, available_copies=None, book_id=None):
            
             
        self.library_id = library_id
        self.title = title
        self.description = description
        self.image_link = image_link
        self.isbn = isbn 
        self.authors = authors
        self.category = category
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.book_id = book_id