import unittest
from tests.base import BaseTest
from app.utils.book_gateway import search_books

class TestBookAdapter(BaseTest):

    def test_book_search_default_filter(self):
        
        book_data = search_books('Programming')

        self.assertIsNotNone(book_data)
        
        if isinstance(book_data, int):
            if book_data == 503:
                self.skipTest('Book API Error: Service Unavailable')
            self.skipTest(f'Book API_Error: Unknown\nStatus Code: {book_data}')

        self.assertIsInstance(book_data, list)
        self.assertIsInstance(book_data[0], dict)
        self.assertGreater(len(book_data), 1)

    def test_book_search_by_author_filter(self):

        book_data = search_books('John', filter='inauthor:')

        if isinstance(book_data, int):
            if book_data == 503:
                self.skipTest('Book API Error: Service Unavailable')
            self.skipTest(f'Book API_Error: Unknown\nStatus Code: {book_data}')

        self.assertIsNotNone(book_data)
        self.assertIsInstance(book_data, list)
        

    def test_book_search_by_isbn(self):
        
        book_data = search_books('9781887902991', filter='isbn:')

        if isinstance(book_data, int):
            if book_data == 503:
                self.skipTest('Book API Error: Service Unavailable')
            self.skipTest(f'Book API_Error: Unknown\nStatus Code: {book_data}')
        
        self.assertIsNotNone(book_data)
        self.assertIsInstance(book_data, list)


    def test_book_search_by_category(self):
        
        book_data = search_books('Computers', filter='subject:')

        if isinstance(book_data, int):
            if book_data == 503:
                self.skipTest('Book API Error: Service Unavailable')
            self.skipTest(f'Book API_Error: Unknown\nStatus Code: {book_data}')
            
        self.assertIsNotNone(book_data)
        self.assertIsInstance(book_data, list)

    def test_book_search_missing_query(self):
        
        with self.assertRaises(TypeError):
            search_books()
        

if __name__ == '__main__':
    unittest.main()