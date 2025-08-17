"""
Book Services
"""
from app.utils.helpers import Helpers
from app.models.book import Books
import requests
from flask import jsonify

class BookManager:

    @staticmethod
    def book_search(query_string):
        url = Helpers.get_book_api(query_string)

        try:

            response = requests.get(url, timeout=5)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            return f"Error:  {e}"
        

        try:

            return response.json()
        
        except ValueError as e:
            return f"Error: {e}"
