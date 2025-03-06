#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary

    Args:
        a_dictionary: the dictionary to modify
        key: the key to delete (always a string)

    Returns:
        The updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
