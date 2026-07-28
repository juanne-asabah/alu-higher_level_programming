#!/usr/bin/python3
"""Defines a text file reading function for standard output streaming."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its raw content straight to stdout.

    Args:
        filename (str): The name of the file to open and read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
