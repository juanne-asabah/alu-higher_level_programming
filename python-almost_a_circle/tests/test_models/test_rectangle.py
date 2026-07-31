#!/usr/bin/python3
"""
This module contains unit tests for the complex operations of Rectangle.
"""
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRectangleOperations(unittest.TestCase):
    """
    Defines test suites to validate rendering, strings, and bulk updates.
    """

    def test_str_output(self):
        """
        Validates the overridden text representation format.
        """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_offsets(self):
        """
        Validates stdout formatting when offsets are omitted.
        """
        r = Rectangle(2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")

    def test_update_args(self):
        """
        Ensures update accepts ordered positional arguments.
        """
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_to_dictionary(self):
        """
        Validates dictionary generation matches spec map keys exactly.
        """
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertDictEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
