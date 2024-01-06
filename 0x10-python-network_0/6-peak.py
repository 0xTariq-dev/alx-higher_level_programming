#!/usr/bin/python3
"""Defining a function that finds a peak in a list of unsorted integers."""


def find_peak(IntList):
    """Function that finds a peak in a list of unsorted integers."""
    if IntList is None or IntList == []:
        return None
    start, end = 0, len(IntList)
    mid = int(((end - start) // 2) + start)

    if end <= 1:
        return IntList[0]
    if end == 2:
        return max(IntList)
    if IntList[mid] > IntList[mid - 1] and IntList[mid] > IntList[mid + 1]:
        return IntList[mid]
    if mid > 0 and IntList[mid] <= IntList[mid + 1]:
        return find_peak(IntList[mid + 1:])
    if mid > 0 and IntList[mid] <= IntList[mid - 1]:
        return find_peak(IntList[:mid - 1])
