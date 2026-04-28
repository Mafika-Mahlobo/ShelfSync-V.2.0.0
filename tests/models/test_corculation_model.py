import unittest
from app import db
from tests.base import BaseTest
from app.models.circulation import ReservationQueue, Loans, Fines
from app.models.book import Books, BookCopies
from app.models.library import Libraries
from app.models.user import Users
from datetime import datetime

class TestCirculation(BaseTest):
    
    def test_reservation_success(self):

        user_data = {
            'name': 'John Doe',
            'email': 'john@email.com',
            'password': 'fwifiwfhi@3jsfjoSD'
        }

        book_data = {
            'title': 'New Book',
            'description': 'ihfiehgoehf\n srjifseigho sgjiegh jighsoghei\n jsehfo girgjse jisohgise jijg\n sjgirjgsp shgioeh jijsg/. srjgiprjs',
            'isbn': '74758477384743',
            'publisher': 'Author, Book sejesgieog'
        }

        library_data = {
            'name': 'Central Library',
            'description': 'ijgprg rsgjojgpsr joerjgg jogpjprjg\n jsifjof gisegj jirjg jopjsg\n jsrijosgi jsgigjs jijsig jijsg\n',
            'location_address': '1562 Springbok street, Johannesburg, South Africa',
            'latitude': -26.10542859042405,
            'longitude': 28.109219037961633
        }

        user_object = Users(
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password']
        )

        book_object = Books(
            title=book_data['title'],
            description=book_data['description'],
            isbn=book_data['isbn'],
            publisher=book_data['publisher']
        )

        library_object = Libraries(
            name=library_data['name'],
            description=library_data['description'],
            location_address=library_data['location_address'],
            latitude=library_data['latitude'],
            longitude=library_data['longitude']
        )

        db.session.add(user_object)
        db.session.add(library_object)
        db.session.add(book_object)
        db.session.commit()

        db_user = Users.query.filter_by(email=user_data['email']).first()
        db_library = Libraries.query.filter_by(name=library_data['name']).first()
        db_book = Books.query.filter_by(isbn=book_data['isbn']).first()

        reservation_object = ReservationQueue(
            user_id=db_user.id,
            book_id=db_book.id,
            library_id=db_library.id,
            position=1
        )

        db.session.add(reservation_object)
        db.session.commit()

        user_reservation = db_user.reservations[0]

        self.assertIsNotNone(user_reservation)
        self.assertEqual(user_reservation.user_id, db_user.id)
        self.assertEqual(user_reservation.book_id, db_book.id)
        self.assertEqual(user_reservation.library_id, db_library.id)
        self.assertEqual(user_reservation.status, 'active')
        self.assertEqual(user_reservation.position, 1),
        self.assertIsInstance(user_reservation.created_at, datetime)
        
    def test_loans_success(self):
        
        user_data = {
            'name': 'John Doe',
            'email': 'john@email.com',
            'password': 'fwifiwfhi@3jsfjoSD'
        }

        book_data = {
            'title': 'New Book',
            'description': 'ihfiehgoehf\n srjifseigho sgjiegh jighsoghei\n jsehfo girgjse jisohgise jijg\n sjgirjgsp shgioeh jijsg/. srjgiprjs',
            'isbn': '74758477384743',
            'publisher': 'Author, Book sejesgieog'
        }

        library_data = {
            'name': 'Central Library',
            'description': 'ijgprg rsgjojgpsr joerjgg jogpjprjg\n jsifjof gisegj jirjg jopjsg\n jsrijosgi jsgigjs jijsig jijsg\n',
            'location_address': '1562 Springbok street, Johannesburg, South Africa',
            'latitude': -26.10542859042405,
            'longitude': 28.109219037961633
        }

        user_object = Users(
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password']
        )

        book_object = Books(
            title=book_data['title'],
            description=book_data['description'],
            isbn=book_data['isbn'],
            publisher=book_data['publisher']
        )

        library_object = Libraries(
            name=library_data['name'],
            description=library_data['description'],
            location_address=library_data['location_address'],
            latitude=library_data['latitude'],
            longitude=library_data['longitude']
        )

        db.session.add(library_object)
        db.session.add(user_object)
        db.session.add(book_object)
        db.session.commit()

        db_library = Libraries.query.filter_by(name=library_data['name']).first()
        db_user = Users.query.filter_by(email=user_data['email']).first()
        db_book = Books.query.filter_by(isbn=book_data['isbn']).first()

        book_copy_object = BookCopies(
            book_id=db_book.id,
            library_id=db_library.id
        )

        db.session.add(book_copy_object)
        db.session.commit()

        db_copy = db_book.copies[0]

        loan_object = Loans(
            user_id=db_book.id,
            copy_id=db_copy.id,
            due_date=datetime(2026, 6, 25, 10, 30, 00)
        )

        db.session.add(loan_object)
        db.session.commit()

        db_loan = Loans.query.filter_by(user_id=db_user.id).first()

        self.assertIsNotNone(db_loan)
        self.assertIsInstance(db_loan.id, int)
        self.assertEqual(db_loan.user_id, db_user.id)
        self.assertEqual(db_loan.copy_id, db_copy.id)
        self.assertIsInstance(db_loan.checkout_date, datetime)
        self.assertIsInstance(db_loan.due_date, datetime)
        self.assertIsInstance(db_loan.created_at, datetime)
        self.assertEqual(db_loan.status, 'active')

    
    def test_fines_success(self):
        pass

if __name__ == '__main__':
    unittest.main()