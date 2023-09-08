#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    n = len(sys.argv) - 1
    operators = {'+', '-', '*', '/'}
    if n == 3:
        a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    elif n != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    if operator not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    if operator == '+':
        print('{} {} {} = {}'.format(a, operator, b, add(a, b)))
    elif operator == '-':
        print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))
    elif operator == '/':
        print('{} {} {} = {}'.format(a, operator, b, div(a, b)))
