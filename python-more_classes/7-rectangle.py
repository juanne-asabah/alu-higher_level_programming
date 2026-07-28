#!/usr/bin/python3
"""Module provides a class definition for a geometric rectangle."""


class Rectangle:
    """Class defining a rectangle with configurable printing characters."""

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This initializes the rectangle and increments the instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter: Retrieve the private width attributes."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width with type and value validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: Retrieve the private height attributes."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height with type and value validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        # Convert symbol to string to handle cases where it is set to another type
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width] * self.__height)

    def __repr__(self):
        """Return a string representation to recreate the instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a termination message and decrement the instance counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
