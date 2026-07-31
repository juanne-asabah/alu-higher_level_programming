#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the maximum value is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Test calling the function with no arguments (uses default list)."""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list consisting entirely of negative integers."""
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test a list with both positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, -3, 0, 4]), 5)


if __name__ == '__main__':
    unittest.main()
