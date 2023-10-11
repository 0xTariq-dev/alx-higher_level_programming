#!/usr/bin/python3
"""Defines student class"""


class Student:
    """Defines a student by (first name, last name and age)"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
