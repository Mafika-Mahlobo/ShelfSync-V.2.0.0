import requests
import json

def search_books(keyword):
    url = f'https://www.googleapis.com/books/v1/volumes?q={keyword}'
    response = requests.get(url)
    data = response.json()
    return data

# Search for books with the keyword "Python"
search_results = search_books('Python')
print(search_results['items'][1]['volumeInfo'])
