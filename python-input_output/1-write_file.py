#!/usr/bin/python3
"""Defines a file-writing function that handles character counting."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and tracks characters written.

    Args:
        filename (str): The name of the file to write or overwrite.
        text (str): The string content to put inside the file.

    Returns:
        int: The precise number of characters committed to the disk file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
