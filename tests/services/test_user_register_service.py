import unittest
from tests.base import BaseTest
from app.services.user.register import add
from app.utils.response import Response

class TestRegister(BaseTest):
    
    def test_user_can_register(self):

        name = 'John Doe'
        email = 'john@shefsync.com'
        password = 'JohnD#Strong29'

        result = add({
                'name': name,
                'email': email,
                'password': password
            })
        
        
        response = result.to_dict()
        
        #Types
        self.assertIsInstance(result, Response)
        self.assertIsInstance(result.data, dict)

        # Success
        self.assertTrue(response['success'])
        self.assertIsNone(response['error'])
        self.assertEqual(response['status_code'], 201)


        # Data
        self.assertEqual(response['data']['name'], name)
        self.assertEqual(response['data']['email'], email)
        self.assertNotIn(password, response)
        self.assertNotIn(password, response['data'])
        self.assertIn('id', response['data'])

        duplicate = add({
                'name': name,
                'email': email,
                'password': password
        })

        duplicate_response = duplicate.to_dict()
        
        self.assertFalse(duplicate_response['success'])
        self.assertIsNotNone(duplicate_response['error'])
        self.assertIsNone(duplicate_response['data'])
        self.assertEqual(duplicate_response['status_code'], 401)


if __name__ == '__main__':
    unittest.main()