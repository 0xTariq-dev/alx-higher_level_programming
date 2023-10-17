#!/usr/bin/python3
""" Defines 4-print_square Model """


def print_square(size):
    """ Method print_square:
    Prints the square size represented by "#" character
    Args:
        size (int): The square length.
    Returns: The square draw.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
