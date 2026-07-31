#!/usr/bin/python3
"""
Defines exhaustive test scenarios targeting the Rectangle model.
"""
import unittest
import io
import sys
import os
from models.rectangle import Rectangle


class TestRectangleAllCases(unittest.TestCase):
    """
    Validates complete edge-case structures of the Rectangle class.
    """

    def test_rectangle_instantiation_zero_height(self):
        """Test of Rectangle(1, 0) exists"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_display_without_x_and_y(self):
        """Test of display() without x and y exists"""
        r = Rectangle(2, 2, 0, 0)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        """Test of display() without y exists"""
        r = Rectangle(2, 2, 2, 0)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "  ##\n  ##\n")

    def test_save_to_file_none(self):
        """Test of Rectangle.save_to_file(None) in Rectangle exists"""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Rectangle.save_to_file([]) in Rectangle exists"""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_valid_list(self):
        """Test of Rectangle.save_to_file([Rectangle(1, 2)]) exists"""
        r = Rectangle(1, 2, 0, 0, 99)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file_no_file(self):
        """Test of Rectangle.load_from_file() when file doesn't exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test of Rectangle.load_from_file() when file exists"""
        r = Rectangle(1, 2, 0, 0, 99)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, 99)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
