#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if len(my_list) >= idx < 0:
        return my_list
    else:
        my_list[idx] = element
