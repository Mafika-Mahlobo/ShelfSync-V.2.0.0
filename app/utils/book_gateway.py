import requests
import os
from dotenv import load_dotenv

load_dotenv()

def search_books(query, filter='intitle:'):
    """Search and normalize book information from google API"""

    params = {
        'key': os.getenv('GOOGLE_API')
    }

    books = []
    url='https://www.googleapis.com/books/v1/volumes?q='

    response = requests.get(url + filter + query, params)
    
    if response.status_code == 200:

        data = response.json()

        book_list = data['items']
        
        for book in book_list:
            books.append({
                'id': book['id'],
                'title': book['volumeInfo'].get('title', None),
                'description': book['volumeInfo'].get('description', None),
                'isbn': book['volumeInfo'].get('industryIdentifiers', None),
                'publisher': book['volumeInfo'].get('publisher', None),
                'authors': book['volumeInfo'].get('authors', None),
                'categories': book['volumeInfo'].get('categories', None)
            })
        
        return books

    return response.status_code

# To-Do: Add Open_library data in search_books function

def get_isbn(works_key):
    
    response = requests.get(f'https://openlibrary.org{works_key}/editions.json')
    pass

def get_authors(author_keys):

    authors = []
    
    if not author_keys == []:
        for key in author_keys:
            
            response = requests.get(f'https://openlibrary.org{key}.json')

            if response.status_code == 200:

                data = response.json()
                authors.append(data.get('name', None))

        return authors
    
    return None


def get_book_metadata(works_key):

    response = requests.get(f'https://openlibrary.org{works_key}.json')

    if response.status_code == 200:

        data = response.json()

        author_keys = [a['author']['key'] for a in data.get('authors')]
        
        description = data.get('description', None)
        isbn, publisher = get_isbn(works_key)
        authors = get_authors(author_keys)
        categories = data.get('subjects', None)
        pass

    pass


def search_open_library(query, filter='title='):
    """Search and normalize book information from Open Library API"""

    books = []
    url = 'https://openlibrary.org/search.json?'

    response = requests.get(url + filter + query)

    if response.status_code == 200:
        
        data = response.json()
        book_list = data.get('docs', [])
        
        for book in book_list:

            key = book['key']
            title = book['title']
            books.append({
                'title': title,
                'id': key
            })
        
        return books

    return response.status_code