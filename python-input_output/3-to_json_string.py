#!/usr/bin/python3
"""Defines a data structure-to-JSON serialization engine function."""
import json


def to_json_string(my_obj):
    """Converts a standard Python object structure into its JSON string form.

    Args:
        my_obj (any): The serializable Python object to transform.

    Returns:
        str: The raw JSON formatted character string representation.
    """
    return json.dumps(my_obj)
