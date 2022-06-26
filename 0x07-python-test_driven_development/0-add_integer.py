#!/usr/bin/python3
"""Define an integer add function."""


def add_integer(a, b=98):
    """Return addition of a and b.
    must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer.
    a and b must be first casted to integers if they are float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
