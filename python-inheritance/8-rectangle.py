#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
The class validates the width and height during instantiation.
"""

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry and validates the
    width and height values, ensuring they are positive integers.
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
