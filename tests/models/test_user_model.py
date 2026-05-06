from app import db
from datetime import datetime
from tests.base import BaseTest
from app.models.user import Users, ActivityLogs
from sqlalchemy.exc import IntegrityError
from tests.helpers import (
    create_user, save_user, create_activity_log, 
    DEFAULT_USER_DATA
)

class TestUserModel(BaseTest):

    def test_user_create_success(self):
        user_data = DEFAULT_USER_DATA
        user_object = create_user()

        # can password hash
        self.assertNotEqual(user_object.password_hash, user_data['password'])

        db.session.add(user_object)
        db.session.commit()

        db_user = Users.query.filter_by(email=user_object.email).first()

        # can save user to db
        self.assertEqual(db_user.name, user_data['name'])
        self.assertEqual(db_user.email, user_data['email'])
        self.assertNotEqual(db_user.password_hash, user_data['password'])

        # derived values
        self.assertIsNotNone(db_user.id)
        self.assertIsNotNone(db_user.created_at)
        self.assertIsNotNone(db_user.updated_at)
        self.assertIsNotNone(db_user.is_active)

        # Types
        self.assertIsInstance(db_user.id, int)
        self.assertIsInstance(db_user.created_at, datetime)
        self.assertIsInstance(db_user.updated_at, datetime)
        self.assertIsInstance(db_user.is_active, bool)

        # To dict
        self.assertEqual(
            db_user.to_dict(),
            {
                'id': 1,
                'name': user_data['name'],
                'email': user_data['email']
            }
        )

    def test_missing_data(self):
        user_data = DEFAULT_USER_DATA
        
        # Missing username
        db.session.add(Users(email=user_data['email'], password=user_data['password']))
        with self.assertRaises(IntegrityError):
             db.session.commit()

        db.session.rollback()

        # Missing email
        db.session.add(Users(name=user_data['name'], password=user_data['password']))
        with self.assertRaises(IntegrityError):
            db.session.commit()

        db.session.rollback()

        # Missing password
        db.session.add(Users(name=user_data['name'], email=user_data['email']))
        with self.assertRaises(IntegrityError):
            db.session.commit()

        db.session.rollback()

        # Empty object
        db.session.add(Users())
        with self.assertRaises(IntegrityError):
            db.session.commit()

        db.session.rollback()

    def test_user_create_duplicate(self):
        user_data = DEFAULT_USER_DATA
        user_object = create_user()

        db.session.add(user_object)
        db.session.commit()

        db.session.add(Users(name=user_data['name'], email=user_data['email'], password=user_data['password']))
        with self.assertRaises(IntegrityError):
            db.session.commit()
        db.session.rollback()

    def test_activity_logging(self):
        db_user = save_user()
        logs_object = create_activity_log(
            user_id=db_user.id,
            action='login'
        )

        self.assertIsNotNone(logs_object)

        db.session.add(logs_object)
        db.session.commit()

        db_logs = ActivityLogs.query.filter_by(user_id=db_user.id).first()
       
        self.assertEqual(db_logs.user_id, 1)
        self.assertEqual(db_logs.action, 'login')
        self.assertIsNotNone(db_logs.timestamp)
        self.assertIsInstance(db_logs.timestamp, datetime)

        # Derived
        self.assertIsNotNone(db_logs.id)
        self.assertIsInstance(db_logs.id, int)