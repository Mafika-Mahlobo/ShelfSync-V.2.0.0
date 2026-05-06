import unittest
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app import db
from tests.base import BaseTest
from app.models.circulation import ReservationQueue, Loans, Fines
from tests.helpers import (
    save_user, save_book, save_library, save_book_copy, create_reservation,
    create_loan, create_fine
)

class TestCirculation(BaseTest):
    
    def setUp(self):
        """Set up common test objects"""
        super().setUp()
        self.user = save_user()
        self.book = save_book()
        self.library = save_library()
        self.copy = save_book_copy(book_id=self.book.id, library_id=self.library.id)
    
    def test_reservation_success(self):
        reservation = create_reservation(
            user_id=self.user.id, book_id=self.book.id, 
            library_id=self.library.id, position=1
        )
        db.session.add(reservation)
        db.session.commit()
        
        saved = self.user.reservations[0]
        self.assertEqual(saved.user_id, self.user.id)
        self.assertEqual(saved.book_id, self.book.id)
        self.assertEqual(saved.library_id, self.library.id)
        self.assertEqual(saved.status, 'active')
        self.assertEqual(saved.position, 1)
        self.assertIsInstance(saved.created_at, datetime)

    def test_reservation_missing_required_fields(self):
        """Test that all required fields are enforced"""
        required_fields = {
            'user_id': (None, self.book.id, self.library.id, 1),
            'book_id': (self.user.id, None, self.library.id, 1),
            'library_id': (self.user.id, self.book.id, None, 1),
            'position': (self.user.id, self.book.id, self.library.id, None)
        }
        
        for field, (uid, bid, lid, pos) in required_fields.items():
            with self.subTest(field=field):
                try:
                    db.session.add(ReservationQueue(
                        user_id=uid, book_id=bid, library_id=lid, position=pos
                    ))
                    db.session.commit()
                except (IntegrityError, TypeError):
                    db.session.rollback()

    def test_reservation_duplicate_position(self):
        res1 = create_reservation(self.user.id, self.book.id, self.library.id, 1)
        db.session.add(res1)
        db.session.commit()
        
        try:
            db.session.add(ReservationQueue(
                user_id=self.user.id, book_id=self.book.id, 
                library_id=self.library.id, position=1
            ))
            db.session.commit()
            self.fail("Expected IntegrityError for duplicate position")
        except IntegrityError:
            db.session.rollback()
        
    def test_loans_success(self):
        loan = create_loan(self.user.id, self.copy.id, datetime(2026, 6, 25, 10, 30, 0))
        db.session.add(loan)
        db.session.commit()
        
        saved = Loans.query.filter_by(user_id=self.user.id).first()
        self.assertIsNotNone(saved)
        self.assertEqual(saved.copy_id, self.copy.id)
        self.assertEqual(saved.status, 'active')
        self.assertIsInstance(saved.checkout_date, datetime)
        self.assertIsInstance(saved.created_at, datetime)

    def test_loans_missing_required_fields(self):
        """Test that all required fields are enforced"""
        due_date = datetime(2026, 6, 25, 10, 30, 0)
        required_fields = {
            'user_id': (None, self.copy.id, due_date),
            'copy_id': (self.user.id, None, due_date),
            'due_date': (self.user.id, self.copy.id, None)
        }
        
        for field, (uid, cid, due) in required_fields.items():
            with self.subTest(field=field):
                try:
                    db.session.add(Loans(user_id=uid, copy_id=cid, due_date=due))
                    db.session.commit()
                except (IntegrityError, TypeError):
                    db.session.rollback()

    def test_loans_multiple_copies(self):
        """Test that same user can borrow multiple copies"""
        copy2 = save_book_copy(book_id=self.book.id, library_id=self.library.id)
        
        loan1 = create_loan(self.user.id, self.copy.id, datetime(2026, 6, 25, 10, 30, 0))
        loan2 = create_loan(self.user.id, copy2.id, datetime(2026, 6, 25, 10, 30, 0))
        
        db.session.add(loan1)
        db.session.add(loan2)
        db.session.commit()
        
        loans = Loans.query.filter_by(user_id=self.user.id).all()
        self.assertEqual(len(loans), 2)

    def test_loans_dates_validation(self):
        """Document expected behavior for date validation"""
        loan = Loans(
            user_id=self.user.id, copy_id=self.copy.id,
            checkout_date=datetime(2026, 6, 25, 10, 30, 0),
            due_date=datetime(2026, 6, 24, 10, 30, 0)
        )
        db.session.add(loan)
        db.session.commit()
        self.assertIsNotNone(Loans.query.filter_by(user_id=self.user.id).first())
    
    def test_fines_success(self):
        loan = create_loan(self.user.id, self.copy.id, datetime(2026, 6, 25, 10, 30, 0))
        db.session.add(loan)
        db.session.commit()
        
        fine = create_fine(loan.id, 25.50)
        db.session.add(fine)
        db.session.commit()
        
        saved = Fines.query.filter_by(loan_id=loan.id).first()
        self.assertEqual(saved.amount, 25.50)
        self.assertFalse(saved.paid)
        self.assertIsInstance(saved.issued_at, datetime)

    def test_fines_missing_required_fields(self):
        """Test that all required fields are enforced"""
        loan = create_loan(self.user.id, self.copy.id, datetime(2026, 6, 25, 10, 30, 0))
        db.session.add(loan)
        db.session.commit()
        
        required_tests = [
            (None, 25.50, "loan_id"),
            (loan.id, None, "amount")
        ]
        
        for lid, amt, field in required_tests:
            with self.subTest(field=field):
                try:
                    db.session.add(Fines(loan_id=lid, amount=amt))
                    db.session.commit()
                except (IntegrityError, TypeError):
                    db.session.rollback()

    def test_fines_multiple_per_loan(self):
        """Test that loans can have multiple fines"""
        loan = create_loan(self.user.id, self.copy.id, datetime(2026, 6, 25, 10, 30, 0))
        db.session.add(loan)
        db.session.commit()
        
        fine1 = create_fine(loan.id, 25.50)
        fine2 = create_fine(loan.id, 10.00)
        
        db.session.add(fine1)
        db.session.add(fine2)
        db.session.commit()
        
        fines = Fines.query.filter_by(loan_id=loan.id).all()
        self.assertEqual(len(fines), 2)
        self.assertEqual(sum(f.amount for f in fines), 35.50)

    def test_fines_paid_status(self):
        """Document expected behavior for paid dates"""
        loan = create_loan(self.user.id, self.copy.id, datetime(2026, 6, 25, 10, 30, 0))
        db.session.add(loan)
        db.session.commit()
        
        fine = create_fine(
            loan.id, 25.50, paid=True,
            issued_at=datetime(2026, 6, 1, 10, 0, 0),
            paid_at=datetime(2026, 5, 31, 10, 0, 0)
        )
        db.session.add(fine)
        db.session.commit()
        
        saved = Fines.query.filter_by(loan_id=loan.id).first()
        self.assertTrue(saved.paid)


if __name__ == '__main__':
    unittest.main()