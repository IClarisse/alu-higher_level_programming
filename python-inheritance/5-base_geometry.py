#!/usr/bin/python3
"""
This module defines the class BaseGeometry.
The class is an empty base class with no functionality.
"""

class BaseGeometry:
    """
    A BaseGeometry class that serves as a base for other geometrical shapes.
    Currently, it does not contain any attributes or methods.
    """
    pass


if __name__ == "__main__":
    # Create an instance of BaseGeometry
    bg = BaseGeometry()

    # Print the instance of the object
    print(bg)

    # Print the list of attributes and methods of the instance
    print(dir(bg))

    # Print the list of attributes and methods of the class itself
    print(dir(BaseGeometry))
