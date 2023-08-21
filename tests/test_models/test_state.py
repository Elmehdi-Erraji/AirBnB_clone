#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))


if __name__ == "__main__":
    unittest.main()
