#!/usr/bin/python3
"""2-square Module:
    A module that defines square"""


class Square:
    """Square:
        Private instance attribute: size, position.
        """

    def __init__(self, size=0, position=(0, 0)):
        '''Instantiation with size and position
        Args:
            size (int): The size of The square, must be 0 or greater.
            position (tuple): Tuple of two positive integers to represent
                the position of the square.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''The getter method of size instantation'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter
        Args:
            value (int): The size of The square, must be 0 or greater
        '''
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        '''The getter method of position instantation'''
        return self.__position

    @position.setter
    def position(self, value):
        '''position setter
        Args:
            value (tuple): Tuple of two positive integers to represent
                the position of the square.
        '''
        if isinstance(value, tuple) and len(value) == 2 and \
         value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

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
            for x in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
