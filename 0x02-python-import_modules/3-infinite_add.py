#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum_arg = 0
    for i in range(1, len(sys.argv)):
        sum_arg += int(sys.argv[i])
    print(sum_arg)
