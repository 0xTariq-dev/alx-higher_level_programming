#!/usr/bin/python3
"""Defines Base Model"""


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
