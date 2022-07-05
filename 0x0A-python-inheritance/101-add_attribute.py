#!/usr/bin/python3
"""define function that adds attributes"""


def add_attribute(obj, att, value):
    """Add new attribute to object
    Args:
      obj (any): object to add attribute
      att (str): attribute's name
      value (any): value of attribute
    Raises:
      TypeError: if attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
