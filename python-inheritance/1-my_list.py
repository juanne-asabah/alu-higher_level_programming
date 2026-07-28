#!/usr/bin/python3
"""Defines a subclass of list called MyList."""


class MyList(list):
    """A custom list class implementing sorted printing."""

    def print_sorted(self):
        """Prints the list items in ascending sorted order."""
        print(sorted(self))
