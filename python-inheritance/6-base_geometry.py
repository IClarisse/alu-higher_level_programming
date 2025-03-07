#!/usr/bin/python3
"""
This module defines the class BaseGeometry.
The class serves as a base for other geometrical shapes.
It contains a public instance method 'area' that raises an exception
indicating that it is not implemented.
"""


class BaseGeometry:
    """
    A BaseGeometry class that serves as a base for other geometrical shapes.
    The class contains an unimplemented area method that should be overridden
    by subclasses.
    """
    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    # Create an instance of BaseGeometry
    bg = BaseGeometry()

    # Try to call the area method which raises an exception
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
