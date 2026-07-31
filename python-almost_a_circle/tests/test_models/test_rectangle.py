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

    def test_instantiation_success(self):
        """Tests valid combinations."""
        r = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 12)

    def test_type_errors(self):
        """Tests strict integer casting guards."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [1])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {}, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, 4.5)

    def test_value_errors(self):
        """Tests geometric limit walls."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -4)

    def test_area_calculation(self):
        """Tests math surface output loops."""
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_str_override(self):
        """Tests text transformations."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_output(self):
        """Tests console graphic captures."""
        r = Rectangle(2, 2, 1, 1)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "\n ##\n ##\n")

    def test_update_positional(self):
        """Tests changing state via sequential args."""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(99, 2, 3, 4, 5)
        self.assertEqual(r.id, 99)
        self.assertEqual(r.width, 2)

    def test_update_keywords(self):
        """Tests changing state via mapped kwargs."""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(height=10, x=5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 5)


if __name__ == "__main__":
    unittest.main()
