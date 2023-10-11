#!/usr/bin/python3
"""Defines load_from_json_file method"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.
    Args:
        filename: The file to read from.
    """
    with open(filename, 'r') as f:
        return json.load(f)
