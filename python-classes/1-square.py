#!/usr/bin/python3
"""This module defines a Square class with a size attribute.

The module provides a foundational blueprint for geometric squares, demonstrating
the use of private instance attributes for proper encapsulation.
"""


class Square:
    """A class that defines a geometric square.

    This class encapsulates the properties of a square, specifically its size,
    ensuring that the attribute is kept private to control future modifications.
    """

    def __init__(self, size):
        """Initialise a new Square instance.

        Args:
            size: The side length of the square. No type or value verification
                is performed during this initialization step.
        """
        self.__size = size
