#!/usr/bin/python3
"""Defines is_kind_of_class function that returns true if it's
same class or subclass."""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class:
    Args:
    a_class: the class to check it's type.
    Returns:
    True if it's same class or subclass or instance otherwise false.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
