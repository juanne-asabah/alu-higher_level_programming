#!/usr/bin/python3
"""Defines a Student class capable of dual-way state preservation updates."""


class Student:
    """Represents a serializable student layout structure framework."""

    def __init__(self, first_name, last_name, age):
        """Initialises a new Student instance structure model.

        Args:
            first_name (str): The given first name of the student.
            last_name (str): The family surname of the student.
            age (int): The recorded numeric age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary overview matching validation limits.

        Args:
            attrs (list): Optional explicit list of string attribute filters.

        Returns:
            dict: The key-value attribute landscape representation.
        """
        if isinstance(attrs, list) and all(type(s) is str for s in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces internal instance variables using external map lookup.

        Args:
            json (dict): A dictionary linking strings to property updates.
        """
        for key, value in json.items():
            setattr(self, key, value)
