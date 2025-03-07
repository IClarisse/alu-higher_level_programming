#!/usr/bin/python3
"""Module that contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or inherited from it,
              False otherwise.
    """
    return isinstance(obj, a_class)
