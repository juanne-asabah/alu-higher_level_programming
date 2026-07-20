#!/usr/bin/python3
"""This module defines a Square class with validation and area calculation.

The module builds upon previous square definitions by introducing a public
method to calculate and return the area of the square instance.
"""


class Square:
    """A class that defines a geometric square.

    This class maintains a private size attribute with strict validation
    and provides a public method to compute the geometric area of the square.
    """

    def __init__(self, size=0):
        """Initialise a new Square instance with validation.

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

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square, which is size squared.
        """
        return self.__size ** 2
