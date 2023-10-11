#!/usr/bin/python3
"""Defines write_file method"""


def write_file(filename="", text=""):
    """Writes a text to a file encoded in 'UTF8' and returns the number
        of characters written.
    Args:
        filename (filestream): The file name to open.
        text (string): The string to write to the file.
    Returns:
        The numbers of characters written.
    """
    with open(filename, mode='w', encoding='UTF8') as f:
        chars = f.write(text)
    return chars
