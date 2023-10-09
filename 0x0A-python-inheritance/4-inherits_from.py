#!/usr/bin/python3
"""Defines inherits_from function that returns true if it is a subclass."""


def inherits_from(obj, a_class):
    """inherits_from:
    Args:
    a_class: the class to check it's type.
    Returns:
    True if it is instance or subclass otherwise false.
    """
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
