#!/usr/bin/python3
"""define a MagiClass as the provided bytecode."""

import math


class MagiClass:
    """Circle representation."""

    def __init__(self, radius=0):
        """Creating a MagiClass.
        Arg:
          radius(float or int): radius of MagiClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return MagiClass area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return MagiClass circumference"""
        return (2 * math.pi * self.__radius)
