#!/usr/bin/python3
"""
This module implements the Rectangle class.

The Rectangle class inherits from Base and defines properties,
getters, setters, geometric area, rendering, and bulk modifications.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle shape that inherits attributes from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance with dimensions and positions.

        Args:
            width (int): The horizontal span of the rectangle.
            height (int): The vertical span of the rectangle.
            x (int): The horizontal offset coordinate.
            y (int): The vertical offset coordinate.
            id (int, optional): The identifier of the geometric entity.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieves the private width attribute of the rectangle instance.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validates and sets the private width attribute of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the private height attribute of the rectangle instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validates and sets the private height attribute of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves the private x coordinate of the rectangle instance.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Validates and sets the private x coordinate of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the private y coordinate of the rectangle instance.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Validates and sets the private y coordinate of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes and returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance to stdout using the '#' character.

        This method respects both the vertical y offset and x margin.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a formatted text representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Assigns positional or key-worded arguments to attributes.

        If *args exists and is not empty, **kwargs will be ignored.
        """
        if args and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                if idx < len(attributes):
                    setattr(self, attributes[idx], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the structured dictionary representation.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
