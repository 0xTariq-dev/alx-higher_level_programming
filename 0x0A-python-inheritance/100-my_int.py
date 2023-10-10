#!/usr/bin/python3
"""Defines class MyInt that inherits from int class"""


class MyInt(int):
    """MyInt:
    Inherits from Rectangle class
    equal sign '==' and not equal '!=' is inverted for this class
    """

    def __eq__(self, other):
        """Equal Method
        Returns:
            Flase if the equal relation is true.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Not Equal Method
        Returns:
            Flase if the not equal relation is true.
        """
        return super().__eq__(other)
