#!/usr/bin/python3
"""Define class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent rectangle using base geometry."""

    def __init__(self, width, height):
        """Initialize a new rectangle.
        Args:
           width (int): rectangle's width
           height (int): rectangle's height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
