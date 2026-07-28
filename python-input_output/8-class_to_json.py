#!/usr/bin/python3
"""Defines a class-to-dictionary mapping utility function."""


def class_to_json(obj):
    """Generates a serializable dictionary description of a class instance.

    Args:
        obj (any): An instance of a custom defined object class structure.

    Returns:
        dict: The internal dictionary lookup attribute namespace mapping.
    """
    return obj.__dict__
