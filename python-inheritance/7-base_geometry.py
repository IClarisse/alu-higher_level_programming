#!/usr/bin/python3
"""
This module defines the class BaseGeometry.
The class contains:
    - area() method: raises an exception for not being implemented.
    - integer_validator() method: validates integers based on provided conditions.
"""

class BaseGeometry:
    """
    A BaseGeometry class that serves as a base for other geometrical shapes.
    It contains:
        - area() method: raises an exception for not being implemented.
        - integer_validator() method: validates integers based on provided conditions.
    """
    
    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if 'value' is an integer and greater than 0.
        
        Args:
            name (str): The name of the variable being validated.
            value (int): The value to be validated.
        
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
