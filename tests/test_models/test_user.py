import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attributes_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_str_method(self):
        expected_str = "[User] ({}) {}".format(self.user.id,
                                               self.user.__dict__)
        self.assertEqual(expected_str, str(self.user))

    def test_save_method(self):
        initial_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(initial_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        self.user.save()
        user_dict = self.user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(
            user_dict['created_at'],
            self.user.created_at.isoformat()
        )
        self.assertEqual(
            user_dict['updated_at'],
            self.user.updated_at.isoformat()
        )
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)

    def test_init_kwargs_with_class_key(self):
        data = {
            '__class__': 'SomeClass',
            'id': '123',
            'created_at': '2023-08-11T20:30:45.123456',
            'updated_at': '2023-08-11T20:30:45.123456'
        }
        obj = User(**data)

        self.assertNotEqual(obj.__class__.__name__, 'SomeClass')
        self.assertEqual(obj.id, '123')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
