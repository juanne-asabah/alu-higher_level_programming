#!/usr/bin/python3
"""
This module defines the Base class.

The Base class serves as the foundation for managing identifiers,
handling JSON/CSV file serialization, and drawing visual shapes.
"""
import json
import os
import csv


class Base:
    """
    Represents the foundational base class for all geometric shapes.

    Attributes:
        __nb_objects (int): Counts active instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance and assigns an identifier.

        Args:
            id (int, optional): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into a standardized JSON string.

        Args:
            list_dictionaries (list): A list of data dictionaries.

        Returns:
            str: The JSON string serialization format representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        The file name is dynamically generated based on the class name.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation into a list of dictionaries.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The deserialized list of dictionary items.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes pre-loaded.

        Args:
            **dictionary (dict): Key-worded attributes to apply.

        Returns:
            Base: A fully initialized subclass instance.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Reads a local JSON file and returns reconstructed instances.

        Returns:
            list: A list of instances reconstructed from the file.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            json_string = f.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of shape objects to a local CSV file format.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]

        with open(filename, "w", newline="", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a local CSV file into an array list of instances.

        Returns:
            list: A collection of dynamically mapped shape instances.
        """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]

        list_objs = []
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=fields)
            for row in reader:
                for key in row:
                    row[key] = int(row[key])
                list_objs.append(cls.create(**row))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a graphics screen using Turtle to draw all shapes.

        Args:
            list_rectangles (list): Rectangle shapes to draw.
            list_squares (list): Square shapes to draw.
        """
        import turtle
        import random

        window = turtle.Screen()
        window.title("Geometric Shapes Framework Canvas")
        window.bgcolor("#ffffff")

        t = turtle.Turtle()
        t.speed(3)
        t.pensize(3)

        colors = ["#ff5733", "#33ff57", "#3357ff", "#f333ff", "#ff33a8"]

        all_shapes = []
        if list_rectangles:
            all_shapes.extend(list_rectangles)
        if list_squares:
            all_shapes.extend(list_squares)

        for shape in all_shapes:
            t.penup()
            t.goto(shape.x, shape.y)
            t.pendown()

            t.color(random.choice(colors))
            t.begin_fill()

            w = shape.width if hasattr(shape, "width") else shape.size
            h = shape.height if hasattr(shape, "height") else shape.size

            for _ in range(2):
                t.forward(w)
                t.left(90)
                t.forward(h)
                t.left(90)

            t.end_fill()

        window.exitonclick()
