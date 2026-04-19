import unittest
from tests.base import BaseTest
from app.services.user.register import add
from app.utils.response import Response

class TestRegister(BaseTest):
    
    def test_add_return_response_instance(self):
        self.ctx = self.app.app_context()
        self.ctx.push()

        result = add({
                'name': 'John Doe',
                'email': 'john@shefsync.com',
                'password': 'JohnD#Strong29'
            })
        
        self.assertIsInstance(result, Response)

if __name__ == '__main__':
    unittest.main()