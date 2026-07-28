#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A geometric square model using equal sides."""

    def __init__(self, size):
        """Initialises a new Square instance.

        Args:
            size (int): The measurement length of a side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
