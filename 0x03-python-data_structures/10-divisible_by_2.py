#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_list = [None] * len(my_list)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            check_list[i] = True
        else: 
            check_list[i] = False
    return check_list
