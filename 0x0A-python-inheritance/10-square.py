#!/usr/bin/python3
"""Define a subclass rectangle square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a square
        Args:
          size (int):square's size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
