#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))


if __name__ == "__main__":
    unittest.main()
