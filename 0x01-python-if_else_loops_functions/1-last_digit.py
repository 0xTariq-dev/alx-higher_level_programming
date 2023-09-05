#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of {} is {} and is {}"
last = number % 10
if number < 0:
    last = -number % 10
if last > 5:
    print(string.format(number, last, 'greater than 5'))
elif 0 < last < 6:
    print(string.format(number, last, 'less than 6 and not 0'))
elif last == 0:
    print(string.format(number, last, '0'))
