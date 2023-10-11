#!/usr/bin/python3
"""Defines save_to_json_file method"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.
    Args:
        my_obj: The obj to serialize.
        filename: The file to write to.
    """
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
