from app import db
from datetime import datetime
from tests.base import BaseTest
from datetime import datetime
from app.models.user import Users, ActivityLogs

class TestUserModel(BaseTest):

    user_data = {
        'name': 'John Doe',
        'email': 'john@email.com',
        'password': 'fwifiwfhi@3jsfjoSD'
    }

    def test_user_create_success(self):
        
        user_object = Users(name=self.user_data['name'], email=self.user_data['email'], password=self.user_data['password'])

        # can create user object
        self.assertEqual(user_object.name, self.user_data['name'])
        self.assertEqual(user_object.email, self.user_data['email'])

        # can password hash
        self.assertNotEqual(user_object.password_hash, self.user_data['password'])

        db.session.add(user_object)
        db.session.commit()

        db_user = Users.query.filter_by(email=user_object.email).first()

        # can save user to db
        self.assertEqual(db_user.name, self.user_data['name'])
        self.assertEqual(db_user.email, self.user_data['email'])
        self.assertNotEqual(db_user.password_hash, self.user_data['password'])

        # derived values
        self.assertIsNotNone(db_user.id)
        self.assertIsNotNone(db_user.created_at)
        self.assertIsNotNone(db_user.updated_at)
        self.assertIsNotNone(db_user.is_active)

        self.assertIsInstance(db_user.id, int)
        self.assertIsInstance(db_user.created_at, datetime)
        self.assertIsInstance(db_user.updated_at, datetime)
        self.assertIsInstance(db_user.is_active, bool)

        # To dict
        self.assertEqual(
            db_user.to_dict(),
            {
                'id': 1,
                'name': self.user_data['name'],
                'email': self.user_data['email']
            }
        )

    def test_activity_logging(self):

        user_object = Users(name=self.user_data['name'], email=self.user_data['email'], password=self.user_data['password'])
        db.session.add(user_object)
        db.session.commit()

        db_user = Users.query.filter_by(email=user_object.email).first()


        logs_object = ActivityLogs(
            user_id=db_user.id,
            action='login',
            timestamp=datetime.now()
        )

        # Logs
        self.assertIsNotNone(logs_object)
        self.assertEqual(logs_object.user_id, 1)
        self.assertEqual(logs_object.action, 'login')
        self.assertIsNotNone(logs_object.timestamp)
        self.assertIsInstance(logs_object.timestamp, datetime)