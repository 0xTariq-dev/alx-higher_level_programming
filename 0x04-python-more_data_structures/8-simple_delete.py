#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        a_dictionary.pop(key, None)
    return a_dictionary 
