import unittest
from tests.base import BaseTest

class TestUserRegister(BaseTest):

    def test_register_route_status_201(self):

        response = self.client.post('/api/users/', json={
            'name': 'Mafika Mahlobo',
            'email': 'mafika@gmaoil.com',
            'password': 'Strongpassword@34'
        })

        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
