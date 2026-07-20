#!/usr/bin/python3
"""This module defines a Square class with getter and setter properties.

The module encapsulates a square's dimensions within a private attribute,
centralising data validation rules through property decorators.
"""


class Square:
    """A class that defines a geometric square.

    This class maintains a private size attribute governed by getter and
    setter methods to safely control its data types and geometric bounds.
    """

    def __init__(self, size=0):
        """Initialise a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The side length of the square instance.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation.

        Args:
            value (int): The new side length for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The geometric area of the square instance.
        """
        return self.__size ** 2
