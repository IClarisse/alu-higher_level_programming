#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle,
which in turn inherits from BaseGeometry.
"""

class BaseGeometry:
    """
    Base class for geometric shapes.
    """

    def area(self):
        """
        Raises an exception because the method should be implemented
        by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.

        Args:
            name (str): The name of the attribute.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry and validates
    the width and height. The area() method is also implemented.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)  # Validate the width
        self.integer_validator("height", height)  # Validate the height
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle in the form:
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
        super().__init__(size, size)  # Use the Rectangle class' __init__ method

    def area(self):
        """
        Returns the area of the square (size * size).
        Inherited from Rectangle's area method.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the square in the form:
        [Rectangle] <size>/<size>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


# Example test case
print(issubclass(Square, Rectangle))  # This should now output True
