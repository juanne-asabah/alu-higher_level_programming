#!/usr/bin/python3
"""Defines a file-to-object deserialization utility function."""
import json


def load_from_json_file(filename):
    """Instantiates a native Python object layout from a structured JSON file.

    Args:
        filename (str): The location path of the JSON file to parse.

    Returns:
        any: The underlying list or dictionary object mapping.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
