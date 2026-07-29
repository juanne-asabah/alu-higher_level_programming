#!/usr/bin/python3
"""Defines a geometry base class with validation logic."""


class BaseGeometry:
    """A base class representing geometry concepts."""

    def area(self):
        """Calculates the geometric area.

        Raises:
            Exception: Always raised to show method is un-implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value argument to ensure it is a positive integer.

        Args:
            name (str): The identifier name of the variable.
            value (int): The numeric variable to validate.

        Raises:
            TypeError: If the value is not a strict integer type.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
