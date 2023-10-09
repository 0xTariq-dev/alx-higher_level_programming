#!/usr/bin/python3
"""Defines is_same_class function that returns true if it's same class only."""


def is_same_class(obj, a_class):
    """is_same_class:
    Args:
    a_class: the class to check it's type.
    Returns:
    True if it's same class otherwise false.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
