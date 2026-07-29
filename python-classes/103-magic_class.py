#!/usr/bin/python3
"""This module defines a MagicClass that mirrors specific Python bytecode.

The class provides structural initialization validation for a hidden radius
attribute and offers mathematical methods for geometric circle calculations.
"""
import math


class MagicClass:
    """A class that replicates specific reverse-engineered Python bytecode.

    This class provides a private radius attribute with strict data type
    constraints, along with calculated geometric attributes of a circle.
    """

    def __init__(self, radius=0):
        """Initialise a new MagicClass instance matching the bytecode steps.

        Args:
            radius (int or float): The radius of the magic instance.
                Defaults to 0.

        Raises:
            TypeError: If the radius is neither an int nor a float.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculate and return the geometric area of the instance.

        Returns:
            float: The area calculated as (radius squared) multiplied by pi.
        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Calculate and return the geometric circumference of the instance.

        Returns:
            float: The circumference calculated as 2 multiplied by pi
                multiplied by the radius.
        """
        return 2 * math.pi * self._MagicClass__radius
