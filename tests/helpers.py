"""Test helpers and factory functions to reduce repetition"""

from app import db
from app.models.user import Users, ActivityLogs
from app.models.library import Libraries, UserLibrary, LibraryHours
from app.models.book import Books, Authors, Categories, BookCopies
from app.models.circulation import ReservationQueue, Loans, Fines
from datetime import datetime


# Default test data dictionaries
DEFAULT_USER_DATA = {
    'name': 'John Doe',
    'email': 'john@email.com',
    'password': 'fwifiwfhi@3jsfjoSD'
}

DEFAULT_BOOK_DATA = {
    'title': 'New Book',
    'description': 'ihfiehgoehf\n srjifseigho sgjiegh jighsoghei\n jsehfo girgjse jisohgise jijg\n sjgirjgsp shgioeh jijsg/. srjgiprjs',
    'isbn': '74758477384743',
    'publisher': 'Author, Book sejesgieog'
}

DEFAULT_LIBRARY_DATA = {
    'name': 'Central Library',
    'description': 'ijgprg rsgjojgpsr joerjgg jogpjprjg\n jsifjof gisegj jirjg jopjsg\n jsrijosgi jsgigjs jijsig jijsg\n',
    'location_address': '1562 Springbok street, Johannesburg, South Africa',
    'latitude': -26.10542859042405,
    'longitude': 28.109219037961633
}

# User factory methods
def create_user(name=None, email=None, password=None, is_active=True):
    """Create and return a user object"""
    user_data = DEFAULT_USER_DATA.copy()
    if name:
        user_data['name'] = name
    if email:
        user_data['email'] = email
    if password:
        user_data['password'] = password
    
    return Users(
        name=user_data['name'],
        email=user_data['email'],
        password=user_data['password'],
        is_active=is_active
    )


def save_user(name=None, email=None, password=None, is_active=True):
    """Create, save, and return a user from database"""
    user = create_user(name, email, password, is_active)
    db.session.add(user)
    db.session.commit()
    return Users.query.filter_by(email=user.email).first()


def create_activity_log(user_id, action='login', timestamp=None):
    """Create and return an activity log object"""
    if timestamp is None:
        timestamp = datetime.now()
    return ActivityLogs(
        user_id=user_id,
        action=action,
        timestamp=timestamp
    )


def save_activity_log(user_id, action='login', timestamp=None):
    """Create, save, and return an activity log"""
    log = create_activity_log(user_id, action, timestamp)
    db.session.add(log)
    db.session.commit()
    return ActivityLogs.query.filter_by(user_id=user_id).first()


# Book factory methods
def create_book(title=None, description=None, isbn=None, publisher=None):
    """Create and return a book object"""
    book_data = DEFAULT_BOOK_DATA.copy()
    if title:
        book_data['title'] = title
    if description:
        book_data['description'] = description
    if isbn:
        book_data['isbn'] = isbn
    if publisher:
        book_data['publisher'] = publisher
    
    return Books(
        title=book_data['title'],
        description=book_data['description'],
        isbn=book_data['isbn'],
        publisher=book_data['publisher']
    )


def save_book(title=None, description=None, isbn=None, publisher=None):
    """Create, save, and return a book from database"""
    book = create_book(title, description, isbn, publisher)
    db.session.add(book)
    db.session.commit()
    return Books.query.filter_by(isbn=book.isbn).first()


def create_author(name):
    """Create and return an author object"""
    return Authors(name=name)


def save_author(name):
    """Create, save, and return an author"""
    author = create_author(name)
    db.session.add(author)
    db.session.commit()
    return Authors.query.filter_by(name=name).first()


def create_category(name):
    """Create and return a category object"""
    return Categories(name=name)


def save_category(name):
    """Create, save, and return a category"""
    category = create_category(name)
    db.session.add(category)
    db.session.commit()
    return Categories.query.filter_by(name=name).first()


# Library factory methods
def create_library(name=None, description=None, location_address=None, latitude=None, longitude=None):
    """Create and return a library object"""
    library_data = DEFAULT_LIBRARY_DATA.copy()
    if name:
        library_data['name'] = name
    if description:
        library_data['description'] = description
    if location_address:
        library_data['location_address'] = location_address
    if latitude:
        library_data['latitude'] = latitude
    if longitude:
        library_data['longitude'] = longitude
    
    return Libraries(
        name=library_data['name'],
        description=library_data['description'],
        location_address=library_data['location_address'],
        latitude=library_data['latitude'],
        longitude=library_data['longitude']
    )


def save_library(name=None, description=None, location_address=None, latitude=None, longitude=None):
    """Create, save, and return a library from database"""
    library = create_library(name, description, location_address, latitude, longitude)
    db.session.add(library)
    db.session.commit()
    return Libraries.query.filter_by(name=library.name).first()


def create_library_hours(library_id, day_of_week, open_time, close_time):
    """Create and return a library hours object"""
    return LibraryHours(
        library_id=library_id,
        day_of_week=day_of_week,
        open_time=open_time,
        close_time=close_time
    )


def save_library_hours(library_id, day_of_week, open_time, close_time):
    """Create, save, and return library hours"""
    hours = create_library_hours(library_id, day_of_week, open_time, close_time)
    db.session.add(hours)
    db.session.commit()
    return LibraryHours.query.filter_by(library_id=library_id, day_of_week=day_of_week).first()


def create_user_library(user_id, library_id, role='member', is_active=True):
    """Create and return a user library membership object"""
    return UserLibrary(
        user_id=user_id,
        library_id=library_id,
        role=role,
        is_active=is_active
    )


def save_user_library(user_id, library_id, role='member', is_active=True):
    """Create, save, and return a user library membership"""
    membership = create_user_library(user_id, library_id, role, is_active)
    db.session.add(membership)
    db.session.commit()
    return UserLibrary.query.filter_by(user_id=user_id, library_id=library_id).first()


# Book copy factory methods
def create_book_copy(book_id, library_id, status='in_stock'):
    """Create and return a book copy object"""
    return BookCopies(
        book_id=book_id,
        library_id=library_id,
        status=status
    )


def save_book_copy(book_id, library_id, status='in_stock'):
    """Create, save, and return a book copy"""
    copy = create_book_copy(book_id, library_id, status)
    db.session.add(copy)
    db.session.commit()
    return BookCopies.query.filter_by(book_id=book_id, library_id=library_id).first()


# Circulation factory methods
def create_reservation(user_id, book_id, library_id, position=1, status='active'):
    """Create and return a reservation queue object"""
    return ReservationQueue(
        user_id=user_id,
        book_id=book_id,
        library_id=library_id,
        position=position,
        status=status
    )


def save_reservation(user_id, book_id, library_id, position=1, status='active'):
    """Create, save, and return a reservation"""
    reservation = create_reservation(user_id, book_id, library_id, position, status)
    db.session.add(reservation)
    db.session.commit()
    return ReservationQueue.query.filter_by(user_id=user_id, book_id=book_id).first()


def create_loan(user_id, copy_id, due_date, status='active', checkout_date=None, return_date=None):
    """Create and return a loan object"""
    if checkout_date is None:
        checkout_date = datetime.now()
    
    return Loans(
        user_id=user_id,
        copy_id=copy_id,
        checkout_date=checkout_date,
        due_date=due_date,
        return_date=return_date,
        status=status
    )


def save_loan(user_id, copy_id, due_date, status='active', checkout_date=None, return_date=None):
    """Create, save, and return a loan"""
    loan = create_loan(user_id, copy_id, due_date, status, checkout_date, return_date)
    db.session.add(loan)
    db.session.commit()
    return Loans.query.filter_by(user_id=user_id, copy_id=copy_id).first()


def create_fine(loan_id, amount, paid=False, issued_at=None, paid_at=None):
    """Create and return a fine object"""
    if issued_at is None:
        issued_at = datetime.now()
    
    return Fines(
        loan_id=loan_id,
        amount=amount,
        paid=paid,
        issued_at=issued_at,
        paid_at=paid_at
    )


def save_fine(loan_id, amount, paid=False, issued_at=None, paid_at=None):
    """Create, save, and return a fine"""
    fine = create_fine(loan_id, amount, paid, issued_at, paid_at)
    db.session.add(fine)
    db.session.commit()
    return Fines.query.filter_by(loan_id=loan_id).first()
