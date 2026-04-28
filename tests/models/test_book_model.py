import unittest
from app import db
from tests.base import BaseTest
from app.models.book import Books, Authors, Categories, BookCopies, book_authors, book_category

class TestBookModel(BaseTest):

    book_data = {
        'title': 'New Book',
        'description': 'ihfiehgoehf\n srjifseigho sgjiegh jighsoghei\n jsehfo girgjse jisohgise jijg\n sjgirjgsp shgioeh jijsg/. srjgiprjs',
        'isbn': '74758477384743',
        'publisher': 'Author, Book sejesgieog'
    }

    def test_add_book_success(self):

        book_object = Books(
            title=self.book_data['title'],
            description=self.book_data['description'],
            isbn=self.book_data['isbn'],
            publisher=self.book_data['publisher']
        )

        # can create book object
        self.assertIsNotNone(book_object)
        self.assertEqual(book_object.title, self.book_data['title'])
        self.assertEqual(book_object.description, self.book_data['description'])
        self.assertEqual(book_object.isbn, self.book_data['isbn'])
        self.assertEqual(book_object.publisher, self.book_data['publisher'])

        db.session.add(book_object)
        db.session.commit()

        db_book = Books.query.filter_by(isbn=self.book_data['isbn']).first()

        # can add book to db
        self.assertIsNotNone(db_book)
        self.assertEqual(db_book.title, self.book_data['title'])
        self.assertEqual(db_book.description, self.book_data['description'])
        self.assertEqual(db_book.isbn, self.book_data['isbn'])
        self.assertEqual(db_book.publisher, self.book_data['publisher'])

        self.assertIsNotNone(db_book.id)

    
    def test_book_author(self):
        
        book_object = Books(
            title=self.book_data['title'],
            description=self.book_data['description'],
            isbn=self.book_data['isbn'],
            publisher=self.book_data['publisher']
        )

        author_object = Authors(
            name='Mafika Mahlobo'
        )

        db.session.add(book_object)
        db.session.commit()

        db_book = Books.query.filter_by(title=self.book_data['title']).first()
        db_book.authors.append(author_object)
        db.session.commit()

        db_authors = db_book.authors[0]

        # Can save book authors association table
        self.assertIsNotNone(db_authors)
        self.assertIsInstance(db_authors.name, str)
        self.assertEqual(db_authors.name, 'Mafika Mahlobo')
        self.assertIsInstance(db_authors.id, int)

    def test_book_category(self):

        book_object = Books(
            title=self.book_data['title'],
            description=self.book_data['description'],
            isbn=self.book_data['isbn'],
            publisher=self.book_data['publisher']
        )

        category_object = Categories(
            name='Sci-Fi'
        )

        db.session.add(book_object)
        db.session.commit()

        db_book = Books.query.filter_by(title=self.book_data['title']).first()
        db_book.categories.append(category_object)
        db.session.commit()

        db_categories = db_book.categories[0]

        self.assertIsNotNone(db_categories)
        self.assertIsInstance(db_categories.id, int)
        self.assertIsInstance(db_categories.name, str)
        self.assertEqual(db_categories.name, 'Sci-Fi')
    

if __name__ == '__main__':
    unittest.main()