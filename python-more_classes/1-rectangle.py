#!/usr/bin/python3
"""This module provides a class definition for a geometric rectangle."""  


class Rectangle:
    """Class defining a rectangle with private width and height attributes."""
    def __init__(self, width=0, height=0):
        """This initializes the rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: Retrieve the private width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width with type and value validatioN"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
           raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: Retrieve the private height attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height with type and value validataion"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
