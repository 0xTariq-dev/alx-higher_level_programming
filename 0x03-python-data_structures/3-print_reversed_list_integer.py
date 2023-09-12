#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list) - 1
    if my_list != None:
        for i in range(n, -1, -1):
            print('{:d}'.format(my_list[i]))
