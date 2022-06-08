#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    car = list(a_dictionary.keys())[0]
    lp = a_dictionary[car]
    for a, b in a_dictionary.items():
        if b > lp:
            lp = b
            car = a
    return car
