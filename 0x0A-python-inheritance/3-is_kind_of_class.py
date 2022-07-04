#!/usr/bin/python3
"""Defines class and inherited class checking function."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance or inherited instance of a_class.
    Args:
      obj (any): object to check
      a_class (type): class to match type
    Returns:
      True if obj is instanxe or inherited instance of a_class
      False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
