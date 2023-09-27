#!/usr/bin/python3
"""2-square Module:
    A module that defines square"""


class Square:
    """Square:
        Private instance attribute: size
        """

    def __init__(self, size=0):
        '''Instantiation with size
        Args:
            size (int): The size of The square, must be 0 or greater
        '''
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        '''Method area: returns the square.

        Returns:
            The square of size.
        '''
        return self.__size ** 2
