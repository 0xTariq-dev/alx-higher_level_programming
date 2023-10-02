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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Instantiation with size
        Args:
            size (int): The size of The square, must be 0 or greater
        '''
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
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

    def my_print(self):
        '''Method my_print: prints the size of square as '#' character.

        Returns:
            The printed area.
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print('#' * self.__size)
