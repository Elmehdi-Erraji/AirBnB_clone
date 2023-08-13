import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        # Clean up any changes made during tests
        self.storage.reload()

    def test_all_method(self):
        # Test the all() method
        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)

    def test_new_method(self):
        # Test the new() method
        self.storage.new(self.base_model)
        obj_key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(obj_key, self.storage.all())

    def test_save_and_reload_methods(self):
        # Test the save() and reload() methods
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        obj_key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(obj_key, self.storage.all())

    def test_reload_method_on_empty_file(self):
         # Test the reload() method when the JSON file is empty
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write('{}')
        self.storage.reload()
        all_objects = self.storage.all()

        # Verify that BaseModel objects are in the dictionary
        self.assertIn(self.base_model, all_objects.values())