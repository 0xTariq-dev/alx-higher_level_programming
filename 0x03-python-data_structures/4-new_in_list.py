#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 or idx < len(my_list):
        new = my_list.copy()
        new[idx] = element
        return new
    else:
        return my_list.copy()
