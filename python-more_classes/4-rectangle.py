#!/usr/bin/python3
"""
Module for rectangle
"""


class Rectangle:
    """
    A class to represent a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle with optional width and height.

        :param width: The width of the rectangle (default is 0).
        :param height: The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The width to set, must be an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: The height to set, must be an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle, or 0 if either dimension is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return the printable representation of the rectangle.
        If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = "\n".join(["#" * self.width
                                   for _ in range(self.height)])
        return rectangle_str

    def __repr__(self):
        """
        Return the string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
