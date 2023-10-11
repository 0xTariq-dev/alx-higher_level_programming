#!/usr/bin/python3
"""Defines student class"""


class Student:
    """Defines a student by (first name, last name and age)"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): The attributes to represent (defaults to None).
        """
        dict = {}
        if attrs is None:
            return self.__dict__
        for x in attrs:
            if hasattr(self, x):
                dict[x] = getattr(self, x)
        return dict

    def reload_from_json(self, json):
        """Replace attributes of student class.

        Args:
            json (dict): The key and value to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
