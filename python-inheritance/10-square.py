#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle,
which in turn inherits from BaseGeometry.
"""

class Square(Rectangle):
    """
    Square class that inherits from Rectangle and validates the size,
    ensuring it's a positive integer.
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
        """
        return super().area()  # Uses Rectangle's area method
