#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))


if __name__ == "__main__":
    unittest.main()
