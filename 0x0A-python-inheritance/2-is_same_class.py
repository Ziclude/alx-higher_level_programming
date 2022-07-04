#!/usr/bin/python3
"""Define a class function of checking."""


def is_same_class(obj, a_class):
    """Check if object is an instance of given class.
    Args:
      obj(ant) : object to check
      a_class (type): class to match type of obj to.
    Returns:
      True if obj is instance of a_class
      False if otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
