#!/usr/bin/python3
"""Defines MyList class that inherites from list class"""


class MyList(list):
    """Class MyList: A subclass of list class"""

    def __init__(self):
        """intialzing method"""
        super().__init__()

    def print_sorted(self):
        """print_sorted: Prints a list in a sorted ascending order"""
        print(sorted(self))
