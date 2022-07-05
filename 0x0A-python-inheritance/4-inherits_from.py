#!/usr/bin/python3
"""Define an inherited class checking function."""


def inherits_from(obj, a_class):
    """Check if object is inherited instance of class.
    Args:
      obj (any): object to check
      a_class (type): class to match object's type
    Returns:
      True if match
      False if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
