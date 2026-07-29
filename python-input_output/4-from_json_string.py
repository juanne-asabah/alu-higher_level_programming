#!/usr/bin/python3
"""Defines a JSON-to-object structural deserialization utility function."""
import json


def from_json_string(my_str):
    """Parses a structured JSON text string into an active Python data model.

    Args:
        my_str (str): The formatted JSON data string to process.

    Returns:
        any: The underlying native Python collection objects represented.
    """
    return json.loads(my_str)
