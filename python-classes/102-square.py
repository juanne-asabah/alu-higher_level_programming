#!/usr/bin/python3
"""This module defines a Square class with area comparison operators.

The module provides full encapsulation for a geometric square, enabling float or
integer dimensions, area calculations, and rich comparison operations between
different square instances based on their area.
"""


class Square:
    """A class that defines a geometric square.

    This class maintains a private size attribute validated for any numeric type.
    It supports area calculation and overrides standard comparison operators
    to allow relative evaluations based on the square's calculated area.
    """

    def __init__(self, size=0):
        """Initialise a new Square instance.

        Args:
            size (int or float): The side length of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int or float: The side length of the square instance.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation.

        Args:
            value (int or float): The new side length for the square.

        Raises:
            TypeError: If the value is not an integer or a float.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int or float: The geometric area of the square instance.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two square areas are equal.

        Args:
            other (Square): The target square instance to compare against.

        Returns:
            bool: True if areas match, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Check if two square areas are not equal.

        Args:
            other (Square): The target square instance to compare against.

        Returns:
            bool: True if areas do not match, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __lt__(self, other):
        """Check if this square's area is less than another square's area.

        Args:
            other (Square): The target square instance to compare against.

        Returns:
            bool: True if this area is strictly smaller, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Check if this square's area is less than or equal to another.

        Args:
            other (Square): The target square instance to compare against.

        Returns:
            bool: True if this area is smaller or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Check if this square's area is greater than another square's area.

        Args:
            other (Square): The target square instance to compare against.

        Returns:
            bool: True if this area is strictly larger, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Check if this square's area is greater than or equal to another.

        Args:
            other (Square): The target square instance to compare against.

        Returns:
            bool: True if this area is larger or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
