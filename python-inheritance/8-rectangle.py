#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A geometry rectangle model using positive integers."""

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
