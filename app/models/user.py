from app import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(length=120), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=128), nullable=False)

    is_active = db.Column(db.Boolean(), default=True, nullable=False)
    created_at = db.Column(db.DateTime(), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    
    membership = db.relationship('UserLibrary', backref='user', cascade='all, delete-orphan')
    reservations = db.relationship('ReservationQueue', backref='user', cascade='all, delete-orphan')
    loans = db.relationship('Loans', backref='user', cascade='all, delete-orphan')
    logs = db.relationship('ActivityLogs', backref='user', cascade='all, delete-orphan')

    @property
    def password(self):
        raise AttributeError('This is not a readable attribute')
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = generate_password_hash(plain_text_password)

    def check_password(self, attempted_password):
        return check_password_hash(self.password_hash, attempted_password)
    
    def __repr__(self):
        return f'<User {self.id} - {self.name}>'
    
class ActivityLogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.Enum('login', 'logout', 'borrow', 'return', 'reserve', 'cancel', name='activity_action', native_enum=False), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
