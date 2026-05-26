import unittest
from tests.base import BaseTest
from tests.helpers import DEFAULT_LIBRARY_DATA
from app.services.library.register import add
from app.utils.response import Response

class TestLibraryRegister(BaseTest):

    def test_library_add_success(self):
        
        response = add(**DEFAULT_LIBRARY_DATA)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.data)

        self.assertEqual(response.data.name, DEFAULT_LIBRARY_DATA['name'])
        self.assertEqual(response.data.description, DEFAULT_LIBRARY_DATA['description'])
        self.assertEqual(response.data.location_address, DEFAULT_LIBRARY_DATA['location_address'])
        self.assertAlmostEqual(float(response.data.latitude), DEFAULT_LIBRARY_DATA['latitude'], places=6)
        self.assertAlmostEqual(float(response.data.longitude), DEFAULT_LIBRARY_DATA['longitude'], places=6)

    def test_duplicate_library(self):
        
        add(**DEFAULT_LIBRARY_DATA)

        with self.assertRaises(ValueError):
            add(**DEFAULT_LIBRARY_DATA)

    def test_invalid_data(self):

        with self.assertRaises(TypeError):
            add({
                'name': 'library_name',
                'email': 'my email',
                'coordinates': -23.75857,
                'location': DEFAULT_LIBRARY_DATA['location_address']
            })

    def test_missing_keys(self):

        with self.assertRaises(TypeError):
            add({
                'name': 'New Library'
            })

if __name__ == '__main__':
    unittest.main()