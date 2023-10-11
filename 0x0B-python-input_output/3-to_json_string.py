#!/usr/bin/python3
"""Defines to_json_string method"""
import json

def to_json_string(my_obj):
    """Serialize an obj as JSON string.
    Args:
        obj: The obj to Serialize.
    Returns:
        The JSON representation of object.
    """
    json_string = json.dumps(my_obj, sort_keys=True)
    return json_string
