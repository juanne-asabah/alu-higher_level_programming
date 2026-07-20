#!/usr/bin/python3
"""This module defines a Square class with custom printing and positioning.

The module provides full encapsulation for a geometric square, allowing users
to instantiate, validate, calculate area, and print the shape using standard
output or string typecasting.
"""


class Square:
    """A class that defines a geometric square.

    This class maintains a private size attribute and a positional tuple
    offset. It supports area calculations, explicit layout printing, and
    direct string typecasting behavior equivalent to its printing method.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
            position (tuple): A tuple containing exactly two positive
                integers representing horizontal and vertical printing
                offsets. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position coordinates of the square.

        Returns:
            tuple: A tuple of two positive integers for structural alignment.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the printing position of the square with tuple checks.

        Args:
            value (tuple): A tuple containing exactly two positive integers.

        Raises:
            TypeError: If value is not a tuple of exactly two elements, or if
                the elements are not integers, or if they are less than 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The geometric area of the square instance.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square instance to stdout using the '#' character.

        The printed square handles horizontal spacing using spaces, and handles
        vertical spacing using empty new lines. If the size of the square is
        equal to 0, this method prints a single empty line instead.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Generate a string representation matching my_print output.

        Returns:
            str: The visual representation of the square layout.
        """
        result = []
        if self.__size == 0:
            return ""

        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            result.append(" * self.__position[0] + "#" * self.__size)

        return "\n".join(result)
