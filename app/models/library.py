from app import db
from datetime import datetime, timezone
from sqlalchemy.orm import validates

class UserLibrary(db.Model):
    __tablename__ = 'user_library'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'), nullable=False, primary_key=True)
    role = db.Column(db.Enum('member', 'admin', name='user_library_role', native_enum=False), nullable=False, default='member')
    joined_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, nullable=False, default=True)


class Libraries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=120), nullable=False)
    description = db.Column(db.Text)
    location_address = db.Column(db.String(50), default='No address', nullable=False)

    latitude = db.Column(db.Numeric(9, 6), nullable=False)
    longitude = db.Column(db.Numeric(9, 6), nullable=False)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    membership = db.relationship('UserLibrary', backref='library', cascade='all, delete-orphan')
    hours = db.relationship('LibraryHours', backref='library', cascade='all, delete-orphan')
    books = db.relationship('BookCopies', backref='library', cascade='all, delete-orphan')
    reservations = db.relationship('ReservationQueue', backref='library', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<library {self.id} - {self.name}>'

class LibraryHours(db.Model):
    __table_args__ = (
        db.UniqueConstraint('library_id', 'day_of_week', name='uq_library_hours_library_day'),
    )

    id = db.Column(db.Integer, primary_key=True)
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'), nullable=False)
    day_of_week = db.Column(db.Enum(
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
        name='day_of_week_enum', native_enum=False
    ), nullable=False)

    open_time = db.Column(db.Time, nullable=False)
    close_time = db.Column(db.Time, nullable=False)

    @validates('open_time', 'close_time')
    def validate_times(self, key, value):
        if key == 'close_time' and hasattr(self, 'open_time') and self.open_time and value <= self.open_time:
            raise ValueError("Close time must be after open time")
        return value