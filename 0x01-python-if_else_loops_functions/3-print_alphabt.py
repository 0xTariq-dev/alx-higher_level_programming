#!/usr/bin/python3
for x in range(97, 123):
    char = chr(x)
    if char != 'e' and char != 'q':
        print(char, end='')
