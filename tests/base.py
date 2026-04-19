import unittest
from app import create_app, db
from app.models import book, library, user, circulation

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.context = self.app.app_context()
        self.client = self.app.test_client()
        self.context.push()

        db.create_all()
    

    def tearDown(self):
        db.session.remove()
        db.drop_all()