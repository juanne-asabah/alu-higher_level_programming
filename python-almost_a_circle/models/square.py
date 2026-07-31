#!/usr/bin/python3
"""
This module implements the Square class.

The Square class inherits directly from Rectangle to represent a shape
with matching width and height dimensions, maintaining symmetry.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape variation of a rectangle matrix.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance using the Rectangle blueprint.

        Args:
            size (int): The uniform measurement of the square.
            x (int): The horizontal offset coordinate.
            y (int): The vertical offset coordinate.
            id (int, optional): The identifier of the geometric entity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieves the uniform size measurement of the square sides.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets both width and height properties using a singular size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a formatted text representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """
        Assigns positional or key-worded arguments to the instance.

        If *args exists and is not empty, **kwargs is ignored.
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for idx, value in enumerate(args):
                if idx < len(attributes):
                    setattr(self, attributes[idx], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the structured dictionary representation of a Square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
