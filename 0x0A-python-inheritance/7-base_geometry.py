#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry:
    raises an Exception with the message area() is not implemented.
    """
    def area(self):
        """area:
        raise Exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator: validates value
        Args:
            name (string): name
            value (int): must be integer and greater than 0
        Raises:
            ValueError: if value is less than or equal to 0.
            TypeError: if value not an integer.
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
