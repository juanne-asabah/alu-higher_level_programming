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

    def test_instantiation_success(self):
        """Tests clean square construction layouts."""
        s1 = Square(5, 1, 0, 3)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 0)

        s2 = Square(5, 1, 2, 3)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 3)

    def test_size_mutation_sync(self):
        """Tests dimensional synchronization behaviors."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_type_errors(self):
        """Tests strict property datatypes validation routing."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, "3")

    def test_value_errors(self):
        """Tests strict limit boundaries for squares metrics."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 2, -3)

    def test_str_override(self):
        """Tests square tracking layouts conversion strings."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_to_dictionary(self):
        """Tests schema matching for square map serializations."""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertDictEqual(s.to_dictionary(), expected)

    def test_create_variants(self):
        """Tests factory creation system variations matching definitions."""
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s2.id, 89)
        self.assertEqual(s2.size, 1)

        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s3.x, 2)

        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s4.y, 3)

    def test_save_to_file_none(self):
        """Tests save_to_file system with None type arguments."""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Tests save_to_file matrix with empty arrays lists."""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_valid(self):
        """Tests save_to_file handling standard list shapes."""
        s = Square(1, 0, 0, 42)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file_no_file(self):
        """Tests load_from_file fallback actions when missing."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Tests loading file outputs arrays list of square shapes."""
        s = Square(2, 0, 0, 42)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, 42)
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
