#!/usr/bin/python3
"""1-Rectangle Module:
    A module that defines rectangle"""


class Rectangle:
    """
    A Rectangle is the product of multiblying a length and width of
        an area.
    """

    def __init__(self, width=0, height=0):
        ''' Instantiation method of rectangle class
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        ''' Property of the width value

        Args:
            value: The width value.
            width must be an integer and greater than or equal to zero.

        Returns: The width.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        ''' Property of the height value

        Args:
            value: The height value.
            height must be an integer and greater than or equal to zero.

        Returns: The height.
        '''
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
