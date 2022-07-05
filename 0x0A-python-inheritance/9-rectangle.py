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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return rectangle's area"""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() representation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
