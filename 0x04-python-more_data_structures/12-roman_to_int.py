#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int = 0
    if not (roman_string and isinstance(roman_string, str)):
        return 0
    else:
        for x in range(len(roman_string)):
            if x > 0 and roman[roman_string[x]] > roman[roman_string[x - 1]]:
                int += roman[roman_string[x]] - 2 * roman[roman_string[x - 1]]
            else:
                int += roman[roman_string[x]]
    return int
