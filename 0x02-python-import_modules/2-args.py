#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = len(sys.argv) - 1
    string = ('{} {}{}'.format(
            n,
            'argument' if n == 1 else 'arguments',
            '.' if n == 0 else ':'
    ))
    print(string)
    if n > 0:
        for i in range(1, n + 1):
            print('{}: {}'.format(i, sys.argv[i]))
