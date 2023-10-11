#!/usr/bin/python3
"""Defines from_json_string method"""
import json


def from_json_string(my_str):
    """Deserialize an obj from JSON string.
    Args:
        my_str: The obj to deserialize.
    Returns:
        The string representation of JSON string.
    """
    string = json.loads(my_str)
    return string
