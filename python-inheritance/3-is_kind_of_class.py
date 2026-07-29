#!/usr/bin/python3
"""Defines a class and inheritance checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if instance or inherited, otherwise False.
    """
    return isinstance(obj, a_class)
