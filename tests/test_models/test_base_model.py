#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(expected_str, str(self.base_model))

    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    """Test Faillure ?"""
    def test_to_dict_method(self):
        self.base_model.save()
        base_model_dict = self.base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            base_model_dict['created_at'],
            self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            base_model_dict['updated_at'],
            self.base_model.updated_at.isoformat()
        )

    def test_init_kwargs_with_class_key(self):
        data = {
            '__class__': 'SomeClass',
            'id': '123',
            'created_at': '2023-08-11T20:30:45.123456',
            'updated_at': '2023-08-11T20:30:45.123456'
        }
        obj = BaseModel(**data)

        self.assertNotEqual(obj.__class__.__name__, 'SomeClass')
        self.assertEqual(obj.id, '123')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
