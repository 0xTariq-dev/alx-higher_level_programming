#!/usr/bin/python3
"""Defines setattr() like method add_attribute"""


def add_attribute(obj, name, value):
    """add_attribute Method
    Args:
        obj : (any) The object to add attribute to.
        name : (string) The attribute name.
        value : The attribute value.
    Returns:
        The new attribute or raise TypeError if failed.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
