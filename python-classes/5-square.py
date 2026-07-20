#!/usr/bin/python3
"""This module defines a Square class with custom printing capabilities.

The module provides full encapsulation for a geometric square, including
validation properties, area calculation, and text-based visual rendering.
"""


class Square:
    """A class that defines a geometric square.

    This class provides robust encapsulation of a square's dimensions,
    allowing developers to safely instantiate, validate, calculate, and print
    the object to standard output.
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

    def my_print(self):
        """Print the square instance to stdout using the '#' character.

        If the size of the square is equal to 0, this method prints
        a single empty line to standard output instead.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
