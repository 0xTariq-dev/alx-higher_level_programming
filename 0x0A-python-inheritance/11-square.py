#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square:
    Inherits from Rectangle class
    """

    def __init__(self, size):
        """Instantiation Method
        Args:
            size (int): The height of the new Rectangle.
        """
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
