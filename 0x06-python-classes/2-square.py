#!/usr/bin/python3
"""2-square Module:
    A module that defines square"""


class Square:
    """Square:
        Private instance attribute: size
        """

    def __init__(self, size=0):
        '''Instantiation with size (no type/value verification)
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
