#!/usr/bin/python3
"""
This module contains unit tests for the Base class serialization features.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBaseSerialization(unittest.TestCase):
    """
    Defines test suites to thoroughly validate the JSON/CSV mechanics of Base.
    """

    def test_automatic_id_assignment(self):
        """
        Tests that ids increment automatically when no value is given.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_explicit_id_assignment(self):
        """
        Tests that explicit ids override automated state increments.
        """
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        """Tests converting a list of dictionaries to a JSON string."""
        d = [{'id': 12, 'width': 10, 'height': 4}]
        json_str = Base.to_json_string(d)
        self.assertEqual(type(json_str), str)

    def test_to_json_string_empty(self):
        """Tests handling of empty and None inputs in serialization."""
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_empty(self):
        """Tests handling of empty strings and None values in parsing."""
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_and_load_file_csv(self):
        """Tests saving objects to a CSV file and reconstructing them."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles_output), 1)
        self.assertEqual(list_rectangles_output[0].width, 10)
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")


if __name__ == "__main__":
    unittest.main()
