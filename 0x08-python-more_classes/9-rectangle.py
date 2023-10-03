#!/usr/bin/python3
"""5-Rectangle Module: A module that defines rectangle"""


class Rectangle:
    """
    A Rectangle is the product of multiblying a length and width of
        an area.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation method of rectangle class
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """print rectangle reprsentation with '#' character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rep = []
        for i in range(self.__height):
            [rep.append(str(self.print_symbol)) for x in range(self.__width)]
            if i != self.__height - 1:
                rep.append("\n")
        return (''.join(rep))

    def __repr__(self):
        """Returns a string representation of the rectangle
            to be able to recreate a new instance"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Detects The deletion of class instance"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns: The biggest rectangle pased on area"""
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        cls.__width = size
        cls.__height = size
        return cls(cls.__width, cls.__height)
