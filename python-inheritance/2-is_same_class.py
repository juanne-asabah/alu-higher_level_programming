#!/usr/bin/python3
"""Defines an exact class checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if exactly an instance, otherwise False.
    """
    return type(obj) is a_class
