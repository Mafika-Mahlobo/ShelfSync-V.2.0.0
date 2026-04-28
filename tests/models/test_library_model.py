import unittest
from app import db
from tests.base import BaseTest
from datetime import datetime, time
from app.models.library import Libraries, UserLibrary, LibraryHours
from app.models.user import Users
from app.models.book import BookCopies, Books

class TestLibraryModel(BaseTest):

    library_data = {
        'name': 'Central Library',
        'description': 'ijgprg rsgjojgpsr joerjgg jogpjprjg\n jsifjof gisegj jirjg jopjsg\n jsrijosgi jsgigjs jijsig jijsg\n',
        'location_address': '1562 Springbok street, Johannesburg, South Africa',
        'latitude': -26.10542859042405,
        'longitude': 28.109219037961633
    }

    def test_library_create_success(self):

        library_object = Libraries(
            name=self.library_data['name'],
            description=self.library_data['description'],
            location_address=self.library_data['location_address'],
            latitude=self.library_data['latitude'],
            longitude=self.library_data['longitude']
        )

        # can create library object
        self.assertIsNotNone(library_object)

        # library object values
        self.assertEqual(library_object.name, self.library_data['name'])
        self.assertEqual(library_object.description, self.library_data['description'])
        self.assertEqual(library_object.location_address, self.library_data['location_address'])
        self.assertEqual(library_object.latitude, self.library_data['latitude'])
        self.assertEqual(library_object.longitude, self.library_data['longitude'])

        db.session.add(library_object)
        db.session.commit()

        db_library = Libraries.query.filter_by(name=self.library_data['name']).first()

        # Can add library
        self.assertIsNotNone(db_library)

        # values
        self.assertEqual(db_library.name, self.library_data['name'])
        self.assertEqual(db_library.description, self.library_data['description'])
        self.assertEqual(db_library.location_address, self.library_data['location_address'])
        self.assertEqual(float(db_library.latitude), round(self.library_data['latitude'], 6))
        self.assertEqual(float(db_library.longitude), round(self.library_data['longitude'], 6))
        
        # derived values
        self.assertIsNotNone(db_library.id)
        self.assertIsNotNone(db_library.created_at)
        self.assertIsNotNone(db_library.updated_at)
        self.assertIsInstance(db_library.id, int)
        self.assertIsInstance(db_library.created_at, datetime)
        self.assertIsInstance(db_library.updated_at, datetime)


    def test_library_hours(self):
        
        library_object = Libraries(
            name=self.library_data['name'],
            description=self.library_data['description'],
            location_address=self.library_data['location_address'],
            latitude=self.library_data['latitude'],
            longitude=self.library_data['longitude']
        )

        db.session.add(library_object)
        db.session.commit()

        db_library = Libraries.query.filter_by(name=self.library_data['name']).first()

        library_hours_object = LibraryHours(
            library_id=db_library.id,
            day_of_week='monday',
            open_time=time(9, 30, 00),
            close_time=time(17, 00 , 00)
        )

        db.session.add(library_hours_object)
        db.session.commit()

        db_hours = LibraryHours.query.filter_by(library_id=db_library.id).first()

        # can add library hours
        self.assertIsNotNone(db_hours)
        self.assertIsNotNone(db_hours.id)
        self.assertEqual(db_hours.library_id, db_library.id)
        self.assertEqual(db_hours.day_of_week, 'monday')
        self.assertEqual(db_hours.open_time, time(9, 30, 00))
        self.assertEqual(db_hours.close_time, time(17, 00, 00))

        # backref
        library = db_hours.library

        self.assertIsNotNone(library)
        self.assertIsInstance(library.id, int)

    def test_library_membership(self):

        user_data = {
            'name': 'John Doe',
            'email': 'john@email.com',
            'password': 'fwifiwfhi@3jsfjoSD'
        }
        
        user_object = Users(name=user_data['name'], email=user_data['email'], password=user_data['password'])
        library_object = Libraries(
            name=self.library_data['name'],
            description=self.library_data['description'],
            location_address=self.library_data['location_address'],
            latitude=self.library_data['latitude'],
            longitude=self.library_data['longitude']
        )

        db.session.add(user_object)
        db.session.add(library_object)
        db.session.commit()

        db_user = Users.query.filter_by(email=user_data['email']).first()
        db_library = Libraries.query.filter_by(name=self.library_data['name']).first()
        
        membership_object = UserLibrary(
            user_id=db_user.id,
            library_id=db_library.id
        )

        # can create membership object
        self.assertIsNotNone(membership_object)
        self.assertEqual(membership_object.user_id, db_user.id)
        self.assertEqual(membership_object.library_id, db_library.id)

        db.session.add(membership_object)
        db.session.commit()

        db_membership = UserLibrary.query.filter_by(user_id=user_object.id).first()

        # can save membership
        self.assertIsNotNone(db_membership)
        self.assertIsInstance(db_membership.user_id, int)
        self.assertIsInstance(db_membership.library_id, int)
        self.assertIsInstance(db_membership.role, str)
        self.assertIsInstance(db_membership.joined_at, datetime)
        self.assertIsInstance(db_membership.is_active, bool)
        self.assertEqual(db_membership.is_active, True)
        self.assertEqual(db_membership.user_id, db_user.id)
        self.assertEqual(db_membership.library_id, db_library.id)
        
    def test_library_book_copy(self):

        book_data = {
            'title': 'New Book',
            'description': 'ihfiehgoehf\n srjifseigho sgjiegh jighsoghei\n jsehfo girgjse jisohgise jijg\n sjgirjgsp shgioeh jijsg/. srjgiprjs',
            'isbn': '74758477384743',
            'publisher': 'Author, Book sejesgieog'
        }
        
        book_object = Books(
            title=book_data['title'],
            description=book_data['description'],
            isbn=book_data['isbn'],
            publisher=book_data['publisher']
        )

        library_object = Libraries(
            name=self.library_data['name'],
            description=self.library_data['description'],
            location_address=self.library_data['location_address'],
            latitude=self.library_data['latitude'],
            longitude=self.library_data['longitude']
        )
        
        db.session.add(book_object)
        db.session.add(library_object)
        db.session.commit()

        db_book = Books.query.filter_by(title=book_data['title']).first()
        db_library = Libraries.query.filter_by(name=self.library_data['name']).first()

        copy_object = BookCopies(
            book_id=db_book.id,
            library_id=db_library.id,
            status='in_stock'
        )

        db.session.add(copy_object)
        db.session.commit()

        db_copy = BookCopies.query.filter_by(book_id=db_book.id).first()

        self.assertIsNotNone(db_copy)
        self.assertEqual(db_copy.book_id, db_book.id)
        self.assertEqual(db_copy.library_id, db_library.id)
        self.assertIsInstance(db_copy.status, str)
        self.assertEqual(db_copy.status, 'in_stock')
        self.assertIsInstance(db_copy.added_at, datetime)


if __name__ == '__main__':
    unittest.main()