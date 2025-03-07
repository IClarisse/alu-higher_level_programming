#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes,
and tracks the number of Rectangle instances.
"""


class Rectangle:
    """Class that defines a rectangle by width and height.

    Attributes:
        number_of_instances (int): Count of Rectangle instances
        print_symbol: Symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): Width value to set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): Height value to set

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)) or 0 if width
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles based on their area.

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle

        Raises:
            TypeError: If rect_1 is not a Rectangle
            TypeError: If rect_2 is not a Rectangle

        Returns:
            Rectangle: The rectangle with the larger area, or rect_1 if equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string of characters forming the rectangle
                 or an empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = []
        for i in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Return a string representation for eval().

        Returns:
            str: A string representation that can recreate the object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
