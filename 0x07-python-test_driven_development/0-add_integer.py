#!/usr/bin/python3
"""
Module 0-add_integer: Adds two integers
The two integers must be int or float else raise Type Error
If one of the parameters is float it will be casted to integer.
"""


def add_integer(a, b=98):
    """ Method add_integer: Adds two numbers
    Args:
        a: first number, b: second number(defaults to 98).
    Returns: The addition of two numbers.
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
