#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines class Rectangle that inherits from BaseGeometry"""


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
