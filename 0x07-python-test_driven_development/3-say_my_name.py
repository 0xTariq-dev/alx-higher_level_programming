#!/usr/bin/python3
""" Defines 3-say_my_name Model """


def say_my_name(first_name, last_name=""):
    """ Method say_my_name:
    Prints the message"My name is <first name> <last name>"
    Args:
        first_name (str): The first name.
        last_name (str)(optional): The last name.
    Returns: The name message.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
