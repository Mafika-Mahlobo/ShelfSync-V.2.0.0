"""
External api function
"""

import requests
import json

def search_books(keyword):

    """
    fetches data from Google books api

    Args:
        keyword (str): search string

    Returns:
        List: list containing book information.
    """

    url = f'https://www.googleapis.com/books/v1/volumes?q={keyword}&maxResults=40'
    all_volume_info = []

    required_keys = ["title", "authors", "publisher", "publishedDate", "description",
                     "industryIdentifiers", "categories", "contentVersion", "imageLinks", "language"]

    try:
        while True:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            books = data.get("items", [])

            for book in books:
                book_info = {}  # Create a new dictionary for each book

                volume_info = book.get("volumeInfo", {})

                # Check if all required keys exist in volume_info
                if all(key in volume_info for key in required_keys):
                    # Extract metadata fields
                    book_info["title"] = volume_info.get("title")
                    book_info["authors"] = volume_info.get("authors")
                    book_info["publisher"] = volume_info.get("publisher")
                    book_info["publishedDate"] = volume_info.get("publishedDate")
                    book_info["description"] = volume_info.get("description")
                    book_info["industryIdentifiers"] = volume_info.get("industryIdentifiers")
                    book_info["categories"] = volume_info.get("categories")
                    book_info["contentVersion"] = volume_info.get("contentVersion")
                    book_info["imageLinks"] = volume_info.get("imageLinks")
                    book_info["language"] = volume_info.get("language")

                    # Append the book_info dictionary to all_volume_info list
                    all_volume_info.append(book_info)

            # Check if there are more pages
            if "nextPageToken" in data:
                url = f'https://www.googleapis.com/books/v1/volumes?q={keyword}&maxResults=40&pageToken={data["nextPageToken"]}'
            else:
                break  # No more pages, exit the loop

    except requests.RequestException as e:
        print("Error fetching books:", e)

    return all_volume_info