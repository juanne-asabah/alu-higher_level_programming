#!/usr/bin/python3
"""Defines a Square class overriding string readouts."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A geometric square model that defines customized string print behavior."""

    def __init__(self, size):
        """Initialises a new Square instance.

        Args:
            size (int): The measurement length of a side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Generates a customized string representation for Square instances."""
        return f"[Square] {self.__size}/{self.__size}"
