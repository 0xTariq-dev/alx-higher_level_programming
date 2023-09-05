#!/usr/bin/python3
for x in range(0, 10):
    for i in range(0, 10):
        if x != i and x < i:
            if x < 8:
                print('{}{}'.format(x, i), end=', ')
            else:
                print('{}{}'.format(x, i))
