#!/usr/bin/python3
"""
Defines exhaustive test scenarios targeting the Square model.
"""
import unittest
import os
from models.square import Square


class TestSquareAllCases(unittest.TestCase):
    """
    Validates complete edge-case structures of the Square class.
    """

    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) in Square exists"""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Square.save_to_file([]) in Square exists"""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_valid_list(self):
        """Test of Square.save_to_file([Square(1)]) in Square exists"""
        s = Square(1, 0, 0, 42)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file_no_file(self):
        """Test of Square.load_from_file() when file doesn't exist"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test of Square.load_from_file() when file exists"""
        s = Square(2, 0, 0, 42)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, 42)
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
