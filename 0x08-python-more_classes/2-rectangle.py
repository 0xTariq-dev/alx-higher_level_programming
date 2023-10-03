#!/usr/bin/python3
"""2-Rectangle Module: A module that defines rectangle"""


class Rectangle:
    """
    A Rectangle is the product of multiblying a length and width of
        an area.
    """

    def __init__(self, width=0, height=0):
        """ Instantiation method of rectangle class
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Get/Set the width value """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get/Set the height value """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns: The rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns: The rectangle perimeter

        Note:
            If width or height is equal to 0 perimeter will be 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
