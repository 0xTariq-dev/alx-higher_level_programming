#!/usr/bin/python3
"""1-square Module:
    A module that defines square"""


class Square:
    """Square:
        Private instance attribute: size
        """

    def __init__(self, size):
        '''Instantiation with size (no type/value verification)
        Args:
            size: The size of The square
        '''
        self.__size = size
