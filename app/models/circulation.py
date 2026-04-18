from app import db
from datetime import datetime, timezone


class ReservationQueue(db.Model):
    __table_args__ = (
        db.UniqueConstraint('book_id', 'library_id', 'position', name='uq_reservation_queue_book_library_position'),
    )


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'),  nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'),  nullable=False)
    status = db.Column(db.Enum('active', 'cancelled', 'fulfilled', name='reservation_status', native_enum=False), nullable=False, default='active')
    position = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

class Loans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),  nullable=False)
    copy_id = db.Column(db.Integer, db.ForeignKey('book_copies.id'),  nullable=False)
    checkout_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    due_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Enum('active', 'returned', 'overdue', name='loan_status', native_enum=False), nullable=False, default='active')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    fines = db.relationship('Fines', backref='loan', cascade='all, delete-orphan')

class Fines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loans.id'),  nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    paid = db.Column(db.Boolean, default=False)
    issued_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    paid_at = db.Column(db.DateTime, nullable=True)