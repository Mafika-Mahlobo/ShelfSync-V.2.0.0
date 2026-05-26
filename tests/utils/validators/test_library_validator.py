import unittest
from tests.base import BaseTest
from tests.helpers import DEFAULT_LIBRARY_DATA
from app.utils.validators.register_validator import LibrarySchema

class TestLibraryValidators(BaseTest):

    def test_library_validator_success(self):
        
        library = LibrarySchema(**DEFAULT_LIBRARY_DATA)

        self.assertIsNotNone(library)
        self.assertIsInstance(library, LibrarySchema)

    def test_missing_data(self):
        
        with self.assertRaises(ValueError) as context:
            LibrarySchema(**{
                'description': 'ijgprg rsgjojgpsr joerjgg jogpjprjg\n jsifjof gisegj jirjg jopjsg\n jsrijosgi jsgigjs jijsig jijsg\n',
                'location_address': '1562 Springbok street, Johannesburg, South Africa',
                'latitude': -26.10542859042405,
                'longitude': 28.109219037961633
            })

        errors = context.exception.errors()

        self.assertIsInstance(errors, list)
        self.assertEqual(errors[0]['type'], 'missing')
        self.assertEqual(errors[0]['loc'], ('name', ))

    def test_invalid_name(self):

        with self.assertRaises(ValueError) as context:
            LibrarySchema(**{
                'name': 'Cen',
                'description': 'ijgprg rsgjojgpsr joerjgg jogpjprjg\n jsifjof gisegj jirjg jopjsg\n jsrijosgi jsgigjs jijsig jijsg\n',
                'location_address': '1562 Springbok street, Johannesburg, South Africa',
                'latitude': -26.10542859042405,
                'longitude': 28.109219037961633
            })

        errors = context.exception.errors()

        self.assertIn('Invalid library name', errors[0]['msg'])

if __name__ == '__main__':
    unittest.main()