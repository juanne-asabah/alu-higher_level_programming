#!/usr/bin/python3
"""This module defines a Square class with custom printing and positioning.

The module encapsulates a square's dimensions and its printing offset position,
ensuring strict data validation via property decorators.
"""


class Square:
    """A class that defines a geometric square.

    This class provides robust encapsulation of a square's size and positional
    offset, offering methods to calculate area and print the shape onto standard
    output with specific horizontal and vertical margins.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a new Square instance with size and positional alignment.

        Args:
            size (int): The side length of the square. Defaults to 0.
            position (tuple): A tuple containing two positive integers representing
                the spacing offsets (horizontal, vertical). Defaults to (0, 0).
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
        return self.__size_position

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
        self.__size_position = value

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

        for _ in range(self.__size_position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__size_position[0] + "#" * self.__size)
