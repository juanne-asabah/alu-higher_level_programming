#!/usr/bin/python3
"""Defines a text appending function for growing existing file streams."""


def append_write(filename="", text=""):
    """Appends text content onto a UTF-8 file and counts characters added.

    Args:
        filename (str): The target file name to find or construct.
        text (str): The explicit data string to append to the end.

    Returns:
        int: The total count of newly appended text layout characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
