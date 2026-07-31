#!/usr/bin/python3
"""
This module contains unit tests for the my_module file.
Tests evaluate edge cases, initialization behaviors, and function logic.
"""
import unittest
from my_module import MyClass


class TestMyClass(unittest.TestCase):
    """
    Defines test suites to thoroughly validate the behaviors of MyClass.
    """

    def test_multiplication(self):
        """
        Tests that my_function correctly multiplies numbers.
        """
        calculator = MyClass(5)
        self.assertEqual(calculator.my_function(3), 15)

    def test_negative_values(self):
        """
        Tests that my_function handles negative multipliers properly.
        """
        calculator = MyClass(5)
        self.assertEqual(calculator.my_function(-2), -10)


if __name__ == '__main__':
    unittest.main()

