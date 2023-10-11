#!/usr/bin/python3
"""Defines read_file method"""


def read_file(filename=""):
    """Reads a text file encoded in 'UTF8' and prints it to stdout
    Args:
        filename (filestream): The file name to open.
    """
    with open(filename, mode='r', encoding='UTF8') as f:
        print(f.read(), end='')
