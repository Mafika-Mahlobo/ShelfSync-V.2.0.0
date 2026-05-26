import unittest
from tests.base import BaseTest
from tests.helpers import DEFAULT_LIBRARY_DATA
from app.utils.response import Response

class TestLibraryRegister(BaseTest):

    def test_library_register_success(self):
        
        response = self.client.post('/api/library/', json=DEFAULT_LIBRARY_DATA)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')

        data = response.get_json()
        self.assertEqual(data['success'], True)

if __name__ == '__main__':
    unittest.main()