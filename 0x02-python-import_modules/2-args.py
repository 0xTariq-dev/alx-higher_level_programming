#!/usr/bin/python3
import sys
n = len(sys.argv)
string = '{} {}{}'.format(
        n,
        'argument' if n == 1 else 'arguments',
        '.' if n == 0 else ':'
)
print(string)
if n != 0:
    for i in range(1, n):
        print('{}: {}'.format(i, sys.argv[i]))
