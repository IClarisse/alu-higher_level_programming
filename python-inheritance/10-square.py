#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle,
which in turn inherits from BaseGeometry. The Square class represents
a square and validates the size during initialization.
"""

from rectangle import Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    This class validates that the size is a positive integer and initializes
    the width and height of the square using the size value. It also calculates
    the area of the square using the inherited area method from the Rectangle class.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the provided size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)  # Validate the size
        # Initialize the parent Rectangle with size for both width and height
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square (size * size).
        Inherited from Rectangle's area method.

        Returns:
            int: The area of the square.
        """
        return super().area()  # Uses Rectangle's area method
