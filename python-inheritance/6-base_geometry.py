#!/usr/bin/python3
"""Defines a geometry base class with stub methods."""


class BaseGeometry:
    """A class representing base geometry structures."""

    def area(self):
        """Calculates area. Not implemented in base class.

        Raises:
            Exception: Always raised with an unimplemented message.
        """
        raise Exception("area() is not implemented")
