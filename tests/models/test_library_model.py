import unittest
from app import db
import warnings
from tests.base import BaseTest
from datetime import time
from app.models.library import Libraries, UserLibrary, LibraryHours
from app.models.book import BookCopies
from sqlalchemy.exc import IntegrityError, SAWarning
from tests.helpers import (
    create_library, save_library, create_library_hours, create_user_library, save_user,
    save_book, create_book_copy, DEFAULT_LIBRARY_DATA
)

class TestLibraryModel(BaseTest):

    def test_library_create_success(self):
        library_data = DEFAULT_LIBRARY_DATA
        library_object = create_library()

        # can create library object
        self.assertIsNotNone(library_object)

        db.session.add(library_object)
        db.session.commit()

        db_library = Libraries.query.filter_by(name=library_data['name']).first()

        # Can add library
        self.assertIsNotNone(db_library)

        # values
        self.assertEqual(db_library.name, library_data['name'])
        self.assertEqual(db_library.description, library_data['description'])
        self.assertEqual(db_library.location_address, library_data['location_address'])
        self.assertEqual(float(db_library.latitude), round(library_data['latitude'], 6))
        self.assertEqual(float(db_library.longitude), round(library_data['longitude'], 6))
        
        # derived values
        self.assertIsNotNone(db_library.id)
        self.assertIsNotNone(db_library.created_at)
        self.assertIsNotNone(db_library.updated_at)
        self.assertIsInstance(db_library.id, int)
        self.assertIsNotNone(db_library.created_at)
        self.assertIsNotNone(db_library.updated_at)

    def test_library_create_missing_data(self):
        library_data = DEFAULT_LIBRARY_DATA
        
        # Missing name
        db.session.add(
            Libraries(
                description=library_data['description'],
                location_address=library_data['location_address'],
                latitude=library_data['latitude'],
                longitude=library_data['longitude']
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()

        db.session.rollback()

        # Missing location address - should have default
        library_object = create_library(name='Test Library 2')
        library_object.location_address = None
        db.session.add(library_object)
        db.session.commit()
        
        db_library = Libraries.query.filter_by(name='Test Library 2').first()
        self.assertEqual(db_library.location_address, 'No address')

        # Missing latitude
        db.session.add(
            Libraries(
                name='Test Library 3',
                description=library_data['description'],
                location_address=library_data['location_address'],
                longitude=library_data['longitude']
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()

        db.session.rollback()

        # Missing longitude
        db.session.add(
            Libraries(
                name='Test Library 4',
                description=library_data['description'],
                location_address=library_data['location_address'],
                latitude=library_data['latitude']
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()

        db.session.rollback()

    def test_library_hours(self):
        db_library = save_library()

        library_hours_object = create_library_hours(
            library_id=db_library.id,
            day_of_week='monday',
            open_time=time(9, 30, 0),
            close_time=time(17, 0, 0)
        )

        db.session.add(library_hours_object)
        db.session.commit()

        db_hours = db_library.hours[0]

        # can add library hours
        self.assertIsNotNone(db_hours)
        self.assertIsNotNone(db_hours.id)
        self.assertEqual(db_hours.library_id, db_library.id)
        self.assertEqual(db_hours.day_of_week, 'monday')
        self.assertEqual(db_hours.open_time, time(9, 30, 0))
        self.assertEqual(db_hours.close_time, time(17, 0, 0))

    def test_library_hours_missing_data(self):
        db_library = save_library()

        # missing library id
        db.session.add(
            LibraryHours(
                day_of_week='monday',
                open_time=time(9, 30, 0),
                close_time=time(17, 0, 0)
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

        # Missing day_of_week
        db.session.add(
            LibraryHours(
                library_id=db_library.id,
                open_time=time(9, 30, 0),
                close_time=time(17, 0, 0)
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

        # Missing open_time
        db.session.add(
            LibraryHours(
                library_id=db_library.id,
                day_of_week='monday',
                close_time=time(17, 0, 0)
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

        # Missing close_time
        db.session.add(
            LibraryHours(
                library_id=db_library.id,
                day_of_week='monday',
                open_time=time(9, 30, 0)
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

    def test_library_hours_duplicate(self):
        db_library = save_library()

        library_hours_object = create_library_hours(
            library_id=db_library.id,
            day_of_week='monday',
            open_time=time(9, 30, 0),
            close_time=time(17, 0, 0)
        )

        db.session.add(library_hours_object)
        db.session.commit()

        db.session.add(
            LibraryHours(
                library_id=db_library.id,
                day_of_week='monday',
                open_time=time(9, 30, 0),
                close_time=time(17, 0, 0)
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

    def test_library_hours_open_after_close(self):
        db_library = save_library()

        with self.assertRaises(ValueError):
            library_hours_object = LibraryHours(
                library_id=db_library.id,
                day_of_week='monday',
                open_time=time(17, 0, 0),
                close_time=time(9, 0, 0)
            )   

    def test_library_membership(self):
        db_user = save_user()
        db_library = save_library()
        
        membership_object = create_user_library(
            user_id=db_user.id,
            library_id=db_library.id
        )

        # can create membership object
        self.assertIsNotNone(membership_object)
        self.assertEqual(membership_object.user_id, db_user.id)
        self.assertEqual(membership_object.library_id, db_library.id)

        db.session.add(membership_object)
        db.session.commit()

        db_membership = UserLibrary.query.filter_by(user_id=db_user.id).first()

        # can save membership
        self.assertIsNotNone(db_membership)
        self.assertIsInstance(db_membership.user_id, int)
        self.assertIsInstance(db_membership.library_id, int)
        self.assertIsInstance(db_membership.role, str)
        self.assertIsNotNone(db_membership.joined_at)
        self.assertIsInstance(db_membership.is_active, bool)
        self.assertEqual(db_membership.is_active, True)
        self.assertEqual(db_membership.user_id, db_user.id)
        self.assertEqual(db_membership.library_id, db_library.id)

    def test_library_membership_missing_data(self):
        db_user = save_user()
        db_library = save_library()
        
        # Missing user_id
        db.session.add(
            UserLibrary(
                library_id=db_library.id
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

        # Missing library_id
        db.session.add(
            UserLibrary(
                user_id=db_user.id
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

    def test_library_membership_duplicate(self):
        
        # Suppress SQLAlchemy warnings for cleaner test output
        warnings.filterwarnings('ignore', category=SAWarning)

        db_user = save_user()
        db_library = save_library()

        membership_object = create_user_library(
            user_id=db_user.id,
            library_id=db_library.id
        )

        db.session.add(membership_object)
        db.session.commit()

        # Try to create duplicate membership
        db.session.add(
            UserLibrary(
                user_id=db_user.id,
                library_id=db_library.id
            )
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()
        
    def test_library_book_copy(self):
        db_book = save_book()
        db_library = save_library()

        copy_object = create_book_copy(
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
        self.assertIsNotNone(db_copy.added_at)


if __name__ == '__main__':
    unittest.main()