import unittest
from tests.base import BaseTest
from app.utils.book_gateway import search_books

class TestBookAdapter(BaseTest):

    def test_book_search_default_filter(self):
        
        book_data = search_books('Programming')

        self.assertIsNotNone(book_data)
        self.assertNotIsInstance(book_data, int)
        self.assertIsInstance(book_data, list)
        self.assertIsInstance(book_data[0], dict)
        self.assertGreater(len(book_data), 1)

    def test_book_search_by_author_filter(self):

        book_data = search_books('John', filter='inauthor:')

        self.assertNotIsInstance(book_data, int)
        self.assertIsNotNone(book_data)
        self.assertIsInstance(book_data, list)
        

    def test_book_search_by_isbn(self):
        
        book_data = search_books('9781887902991', filter='isbn:')

        self.assertNotIsInstance(book_data, int)
        self.assertIsNotNone(book_data)
        self.assertIsInstance(book_data, list)


    def test_book_search_by_category(self):
        
        book_data = search_books('Computers', filter='subject:')

        self.assertNotIsInstance(book_data, int)
        self.assertIsNotNone(book_data)
        self.assertIsInstance(book_data, list)

    def test_book_search_missing_query(self):
        
        with self.assertRaises(TypeError):
            search_books()
        

if __name__ == '__main__':
    unittest.main()