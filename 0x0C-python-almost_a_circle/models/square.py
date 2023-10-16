#!/usr/bin/python3
"""Defines Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square:
    Inherits from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation Method
        Args:
            size (int): The size of the new square.
            x (int)(default = 0)
            y (int)(default = 0)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size value"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
