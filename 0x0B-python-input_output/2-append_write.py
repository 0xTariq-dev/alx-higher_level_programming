#!/usr/bin/python3
"""Defines append_write method"""


def append_write(filename="", text=""):
    """Appends a text to the end of file encoded in 'UTF8' and returns the number
        of characters added.
    Args:
        filename (filestream): The file name to open.
        text (string): The string to write to the file.
    Returns:
        The numbers of characters added.
    """
    with open(filename, mode='a', encoding='UTF8') as f:
        chars = f.write(text)
    return chars
