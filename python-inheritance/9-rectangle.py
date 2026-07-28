#!/usr/bin/python3
"""Defines a fully implemented Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A geometry rectangle model capable of computing its space."""

    def __init__(self, width, height):
        """Initialises a new Rectangle instance.

        Args:
            width (int): The horizontal span of the rectangle.
            height (int): The vertical span of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes and returns the area of the rectangle instance."""
        return self.__width * self.__height

    def __str__(self):
        """Generates a friendly string overview representation."""
        return f"[Rectangle] {self.__width}/{self.__height}"
