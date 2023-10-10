#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle:
    Inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        """Instantiation Method
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Calculates The area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Defins the print() and str() methods behavior"""
        description = "[" + str(self.__class__.__name__) + "]"
        description += str(self.__width) + "/" + str(self.__height)
        return description
