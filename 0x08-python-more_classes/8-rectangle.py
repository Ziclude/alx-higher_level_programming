#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent rectangle.
    Args:
      number_of_instances (int): Rectangle instances number.
      print_symbol (any): Representation symbol
"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a new rectangle.
        Args:
           width (int): width of rectangle
           height (int): height of rectangle
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return rectangle with greater area.
        Args:
          rect_1 (Rectangle): first rectangle
          rect_2 (Rectangle): second rectangle
        Raises:
          TypeError: If one isn't a rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Return and represents rectangle with # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectan = []
        for a in range(self.__height):
            [rectan.append(str(self.print_symbol)) for
             b in range(self.__width)]
            if a != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """String representation of rectangle"""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """Print message for every deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
