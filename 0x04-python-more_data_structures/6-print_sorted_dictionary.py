#!/usr/bin/python3
"""print dictionary by ordered keys"""
def print_sorted_dictionary(a_dictionary):
    for a in sorted(a_dictionary):
        print("{}: {}".format(a, a_dictionary[a]))
