#!/usr/bin/python3
"""Print square with character #."""


def print_square(size):
    """ Print a square with # character.
    Args:
       size (int): height and width of a square.
    Raises:
       TypeError: Size isn't integer.
       ValueError: Size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        [print("#", end="") for b in range(size)]
        print("")
