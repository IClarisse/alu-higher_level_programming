#!/usr/bin/python3
"""
This module defines the class BaseGeometry.
The class contains the method 'area' that raises an exception
indicating that it is not implemented, and an 'integer_validator'
method to validate integers based on the specified conditions.
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


if __name__ == "__main__":
    # Create an instance of BaseGeometry
    bg = BaseGeometry()

    # Valid integer validation
    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    # Test invalid values
    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
