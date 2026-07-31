#!/usr/bin/python3
"""
This module provides a function `print_square` that prints a square grid
composed of the '#' character based on a given size length.
"""


def print_square(size=None):
    """
    Prints a square with the character #.

    Args:
        size: The side length of the square (must be an integer).

    Raises:
        TypeError: If size is not an integer, or if it is a float less than 0.
        ValueError: If size is an integer less than 0.
    """
    if size is None:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int) or type(size) is bool:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
