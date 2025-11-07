from werkzeug.security import generate_password_hash, check_password_hash
from app.config import book_api2, book_api1
import requests

class Helpers:

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    
    
    @staticmethod
    def book_search(query_string):
        url1 = f"{book_api1}{query_string}"
        url2 = f"{book_api2}{query_string}&maxResults=20"

        try:

            open_library = requests.get(url1, timeout=5)
            google_books = requests.get(url2, timeout=5)

        except requests.exceptions.RequestException as e:
            return f"Error:  {e}"
        

        try:

            api1 = open_library.json()
            api2 = google_books.json()

            return {"open_library": api1, "google_books": api2}
        
        except ValueError as e:
            return f"Error: {e}"
        
    @staticmethod
    def books_info(query):

        books = []
        get_book = Helpers.book_search(query)["google_books"]["items"]
        allowed = ("title", "authors", "industryIdentifiers", "imageLinks", "description", "categories")

        for book in get_book:
            if "id" in book and all(k in book["volumeInfo"] for k in allowed):
                books.append( {"id": book["id"],
                               "title": book["volumeInfo"]["title"],
                               "authors": book["volumeInfo"]["authors"],
                               "isbn_number":  book["volumeInfo"]["industryIdentifiers"][0]["identifier"],
                               "images":  book["volumeInfo"]["imageLinks"],
                               "description":  book["volumeInfo"]["description"],
                               "categories":  book["volumeInfo"]["categories"]
                               })

        return books