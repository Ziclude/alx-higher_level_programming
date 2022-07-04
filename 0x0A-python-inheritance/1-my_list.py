#!/usr/bin/python3
"""Contains my list class"""


class MyList(list):
    """a class of list"""
    def __init__(self):
        """initializes object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
