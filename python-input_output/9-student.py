#!/usr/bin/python3
"""Defines a Student data structure class template model."""


class Student:
    """Represents a standard student structure by profile attributes."""

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

    def to_json(self):
        """Retrieves a pure dictionary representation of a Student instance."""
        return self.__dict__
