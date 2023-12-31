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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the instance"""
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args):
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
