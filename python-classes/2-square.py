#!/usr/bin/python3
"""This module defines a Square class with type and value validation.

The module ensures that any created Square instance has a valid, non-negative
integer size, promoting data integrity and robust object-oriented design.
"""


class Square:
    """A class that defines a geometric square.

    This class enforces strict encapsulation and data validation by ensuring
    the size attribute is an integer and is greater than or equal to zero.
    """

    def __init__(self, size=0):
        """Initialise a new Square instance with type and value checks.

        Args:
            size (int): The side length of the square. Defaults to 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
