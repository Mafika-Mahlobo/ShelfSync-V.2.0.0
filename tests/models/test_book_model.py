import unittest
from app import db
from tests.base import BaseTest
from sqlalchemy.exc import IntegrityError
from app.models.book import Books, Authors, Categories
from tests.helpers import (
    create_book, save_book, create_author, create_category, DEFAULT_BOOK_DATA
)

class TestBookModel(BaseTest):

    def test_add_book_success(self):
        book_data = DEFAULT_BOOK_DATA
        book_object = create_book()

        # can create book object
        self.assertIsNotNone(book_object)

        db.session.add(book_object)
        db.session.commit()

        db_book = Books.query.filter_by(isbn=book_data['isbn']).first()

        # can add book to db
        self.assertIsNotNone(db_book)
        self.assertEqual(db_book.title, book_data['title'])
        self.assertEqual(db_book.description, book_data['description'])
        self.assertEqual(db_book.isbn, book_data['isbn'])
        self.assertEqual(db_book.publisher, book_data['publisher'])

        # Derived values
        self.assertIsNotNone(db_book.id)
        self.assertIsInstance(db_book.id, int)

    def test_add_book_missing_data(self):
        book_data = DEFAULT_BOOK_DATA

        # Missing title
        db.session.add(
            Books(
            description=book_data['description'],
            isbn=book_data['isbn'],
            publisher=book_data['publisher']
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()

        db.session.rollback()

        # Missing isbn
        db.session.add(
            Books(
                title=book_data['title'],
                description=book_data['description'],
                publisher=book_data['publisher']
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        
        db.session.rollback()

    def test_book_duplicate(self):
        book_data = DEFAULT_BOOK_DATA
        book_object = create_book()

        db.session.add(book_object)
        db.session.commit()

        db.session.add(
            Books(
                title=book_data['title'],
                description=book_data['description'],
                isbn=book_data['isbn'],
                publisher=book_data['publisher']
            )
        )

        with self.assertRaises(IntegrityError):
            db.session.commit()
    
    def test_book_author(self):
        book_data = DEFAULT_BOOK_DATA
        db_book = save_book()
        
        author_object = create_author('Mafika Mahlobo')
        db_book.authors.append(author_object)
        db.session.commit()

        db_authors = db_book.authors[0]

        # Can save book authors association table
        self.assertIsNotNone(db_authors)
        self.assertIsInstance(db_authors.name, str)
        self.assertEqual(db_authors.name, 'Mafika Mahlobo')
        self.assertIsInstance(db_authors.id, int)

    def test_author_missing_data(self):
        db_book = save_book()
        
        # Missing name
        author_object = Authors()
        db_book.authors.append(author_object)

        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_author_duplicate(self):
        db_book = save_book()
        author_object = create_author('Mafika Mahlobo')
        db_book.authors.append(author_object)
        db.session.commit()

        db_book.authors.append(author_object)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_book_category(self):
        db_book = save_book()
        category_object = create_category('Sci-Fi')

        db_book.categories.append(category_object)
        db.session.commit()

        db_categories = db_book.categories[0]

        self.assertIsNotNone(db_categories)
        self.assertIsInstance(db_categories.id, int)
        self.assertIsInstance(db_categories.name, str)
        self.assertEqual(db_categories.name, 'Sci-Fi')

    def test_category_missing_data(self):
        db_book = save_book()
        
        # Missing name
        category_object = Categories()
        db_book.categories.append(category_object)

        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_category_duplicate(self):
        db_book = save_book()
        category_object = create_category('Sci-Fi')

        db_book.categories.append(category_object)
        db.session.commit()

        # Duplicate
        db.session.add(Categories(
            name='Sci-Fi'
        ))
        
        with self.assertRaises(IntegrityError):
            db.session.commit()

if __name__ == '__main__':
    unittest.main()