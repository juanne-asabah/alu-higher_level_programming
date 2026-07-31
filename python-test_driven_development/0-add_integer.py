#!/usr/bin/python3
"""
This module provides a function `add_integer` that adds two numbers.
It accepts integers and floats, casting floats to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float), defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float,
                   or if they are NaN/Infinity values.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if (a != a) or (a in [float('inf'), float('-inf')]):
        raise TypeError("a must be an integer")
    if (b != b) or (b in [float('inf'), float('-inf')]):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
