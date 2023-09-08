#!/usr/bin/python3
import sys
if __name__ == 'main':
    
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
