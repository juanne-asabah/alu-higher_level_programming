#!/usr/bin/python3
"""
This module provides a function `text_indentation` that parses text and
adds two new lines after specific punctuation characters: `.`, `?`, and `:`.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: A string containing the text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length and text[i] == ' ':
        i += 1

    while i < length:
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
