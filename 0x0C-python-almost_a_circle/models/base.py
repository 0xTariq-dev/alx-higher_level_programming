#!/usr/bin/python3
"""Defines Base Model"""
import json


class Base:
    """Base class

    The Base Class for all classes in this package

    private class attribute:
        __nb_object (int): Counter for the instances of the class.
    """

    __nb_objects = 0  # Number of objects insatatiated from the class.

    def __init__(self, id=None):
        """Instatiation Method

        Args:
            id (int)(optional): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list of dictionaries

        Args:
            list_dictionaries (list): list of dicts for instances.
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_obj (list): list of objects to write to the file.
        """
        json_file = cls.__name__ + ".json"
        with open(json_file, "w") as j:
            if list_objs is None:
                j.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                j.write(Base.to_json_string(dicts))
