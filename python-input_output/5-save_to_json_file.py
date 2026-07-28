#!/usr/bin/python3
"""Defines an object-to-file serialization utility function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object directly to a text file using its JSON representation.

    Args:
        my_obj (any): The data structure to serialize.
        filename (str): The target file destination pathway.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
