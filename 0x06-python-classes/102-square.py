#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Collect current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of the square."""
        return (self.__size * self.__size)

    def __qe__(self, other):
        """equals comparison"""
        return self.area() == other.area()

    def __non__(self, other):
        """Not comparison"""
        return self.area() != other.area()

    def __les__(self, other):
        """inferior comparison"""
        return self.area() < other.area()

    def __leseq__(self, other):
        """Inferior or equals comparison"""
        return self.area() <= other.area()

    def __sup__(self, other):
        """equals comparison"""
        return self.area() > other.area()

    def __supeq__(self, other):
        """Superior or equals comparison"""
        return self.area() >= other.area()
