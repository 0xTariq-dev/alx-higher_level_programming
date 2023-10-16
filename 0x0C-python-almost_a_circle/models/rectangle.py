#!/usr/bin/python3
"""Defines Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle:
    Inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation Method
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int)(default = 0)
            y (int)(default = 0)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter Method for width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter Method for width attribute"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Getter Method for height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter Method for height attribute"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter Method for x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter Method for x attribute"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter Method for y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter Method for y attribute"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Returns: The area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints The area of rectangle with '#' character to stdout"""
        for i in range(self.__y):
            print('')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """Returns a string representation of the class instance"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" + \
               f" - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the instance"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args):
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
