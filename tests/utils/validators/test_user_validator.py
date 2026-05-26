import unittest
from tests.base import BaseTest
from app.utils.validators.register_validator import UserSchema
from tests.helpers import DEFAULT_USER_DATA

class TestUserValidators(BaseTest):
    
    def test_user_validation_success(self):

        user = UserSchema(**DEFAULT_USER_DATA)

        self.assertIsNotNone(user)
        self.assertIsInstance(user, UserSchema)

    def test_missing_data(self):

        with self.assertRaises(ValueError) as context:
            UserSchema(**{
                'name': 'John Doe',
                'email': 'john@email.com',
                'password': 'fwifiwfhi@3jsfjoSD'
            })

        errors = context.exception.errors()

        self.assertIsInstance(errors, list)
        self.assertEqual(errors[0]['type'], 'missing')
        self.assertEqual(errors[0]['loc'], ('confirm_password',))

    def test_password_not_match(self):

        with self.assertRaises(ValueError) as context:
            UserSchema(**{
                'name': 'John Doe',
                'email': 'john@email.com',
                'password': 'fwifiwfhi@3jsfjoSD',
                'confirm_password': 'fwifiwfhdf3jsfjoSD'
            })

        errors = context.exception.errors()

        self.assertIsInstance(errors, list)
        self.assertEqual(errors[0]['type'], 'value_error')
        self.assertIn('Passwords do not match', errors[0]['msg'])


if __name__ == '__main__':
    unittest.main()