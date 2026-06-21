import unittest
from tests.base import BaseTest
from app.services.user.register import add
from app.services.user.login import login
from app.utils.response import Response

class TestUserAuth(BaseTest):

    def test_login_success(self):

        user_data = {
            'name': 'John Doe',
            'email': 'john@shefsync.com',
            'password': 'JohnD#Strong29'
        }

        add(**user_data)
        user_data.pop('name', None)

        response = login(**user_data)
        

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        

if __name__ == '__main__':
    unittest.main()