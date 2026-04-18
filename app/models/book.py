from app import db
from datetime import datetime, timezone


book_authors = db.Table( 
    'book_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), nullable=False, primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), nullable=False, primary_key=True)
    )


book_category = db.Table(
    'book_category',
     db.Column('book_id', db.Integer, db.ForeignKey('books.id'), nullable=False, primary_key=True),
     db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), nullable=False, primary_key=True)
    )

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.String(length=20), nullable=False, unique=True)
    publisher = db.Column(db.String(length=200))

    authors = db.relationship('Authors', secondary=book_authors, backref='books')
    categories = db.relationship('Categories', secondary=book_category, backref='books')
    copies = db.relationship('BookCopies', backref='book', cascade='all, delete-orphan')

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False, unique=True)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(length=100), nullable=False, unique=True)

class BookCopies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'), nullable=False)
    status = db.Column(db.Enum('in_stock', 'checked_out', name='book_copy_status', native_enum=False), nullable=False, default='in_stock')
    added_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    loans = db.relationship('Loans', backref='copy')