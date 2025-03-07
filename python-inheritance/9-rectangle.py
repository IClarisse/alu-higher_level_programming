#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry
and implements the area() method.
"""


class BaseGeometry:
    """
    Base class with common geometry validation methods.
    """

    def area(self):
        """Raises an exception when not implemented in the subclass."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry and validates the
    width and height values, ensuring they are positive integers.
    Implements the area method to calculate the area of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the provided width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        # Private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format:
        [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
