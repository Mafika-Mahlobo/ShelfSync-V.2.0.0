from app import create_app, db
from tests.base import BaseTest
from app.models.user import Users, ActivityLogs

class TestUserModel(BaseTest):

    def test_user_create_success(self):
        pass