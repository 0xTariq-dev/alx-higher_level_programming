#!/usr/bin/python3
"""Defines pascal_traingle method"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s
        triangle of n.

    Args:
        n (int): The number to get pascal's traingle for.
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        triangle = pascal[-1]
        temp = [1]
        for x in range(len(triangle) - 1):
            temp.append(triangle[x] + triangle[x + 1])
        temp.append(1)
        pascal.append(temp)
    return pascal
