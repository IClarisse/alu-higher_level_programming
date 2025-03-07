#!/usr/bin/python3
"""
Module for Square class
This module contains the definition of a Square class that inherits
from the Rectangle class. The Square class represents a geometric
square with equal sides.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    
    This class represents a square, which is a special case of a rectangle
    where all sides are equal. It inherits from the Rectangle class and
    implements specific behavior for squares.
    
    Attributes:
        __size (int): The size of the square sides
    """

    def __init__(self, size):
        """
        Initialize a Square instance
        
        Args:
            size (int): Size of the square (positive integer)
        
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square
        
        Returns:
            int: The area of the square (size squared)
        """
        return self.__size ** 2
