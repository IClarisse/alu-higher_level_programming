#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute,
validation, and an area method
"""


class Square:
    """
    Class that defines a square by its size
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance with optional size

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: The area of the square (size squared)
        """
        return self.__size ** 2
