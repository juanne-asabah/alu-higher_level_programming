#!/usr/bin/python3
"""
This module contains unit tests for the Square class.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Defines test cases targeting the Square initialization and size overrides.
    """

    def test_square_instantiation(self):
        """
        Tests symmetry and properties inherited from Rectangle.
        """
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_size_getter_setter(self):
        """
        Validates that altering size shifts both internal dimensions.
        """
        s = Square(4)
        s.size = 8
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

    def test_square_update_args(self):
        """
        Validates positional updates on a Square instance.
        """
        s = Square(5, 0, 0, 1)
        s.update(10, 7, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


if __name__ == "__main__":
    unittest.main()
