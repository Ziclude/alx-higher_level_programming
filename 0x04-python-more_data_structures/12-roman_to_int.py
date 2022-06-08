#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    my_dictio = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numb = 0
    for a in range(len(roman_string)):
        if my_dictio.get(roman_string[a], 0) == 0:
            return 0
        if (a != (len(roman_string) - 1) and my_dictio[roman_string[a]] < my_dictio[roman_string[a + 1]]):
            numb += my_dictio[roman_string[a]] * -1
        else:
            numb += my_dictio[roman_string[a]]
    return (numb)
