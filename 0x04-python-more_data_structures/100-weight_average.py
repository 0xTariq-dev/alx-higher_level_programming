#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_weight, value = 0, 0
    for score, weight in my_list:
        sum_weight += weight
        value += (score * weight)
    return value / sum_weight
        

