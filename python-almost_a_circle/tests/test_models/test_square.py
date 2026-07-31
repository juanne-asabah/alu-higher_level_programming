#!/usr/bin/python3
"""
Defines exhaustive test scenarios targeting the Square model.
"""
import unittest
from models.square import Square


class TestSquareAllCases(unittest.TestCase):
    """
    Validates complete edge-case structures of the Square class.
    """

    def test_instantiation_success(self):
        """Tests clean square construction layouts."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

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
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(5)
            s.size = "10"

    def test_value_errors(self):
        """Tests strict limits for square sizes."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_str_override(self):
        """Tests square tracking layouts conversion strings."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_mixed(self):
        """Tests square dynamic updates loops properties."""
        s = Square(1, 1, 1, 1)
        s.update(99, 4, y=10)  # args overrides kwargs entirely
        self.assertEqual(s.id, 99)
        self.assertEqual(s.size, 4)


if __name__ == "__main__":
    unittest.main()
