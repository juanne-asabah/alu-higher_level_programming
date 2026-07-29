#!/usr/bin/python3
"""Defines an inherited class checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a subclass (direct/indirect).

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if it strictly inherits from a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
