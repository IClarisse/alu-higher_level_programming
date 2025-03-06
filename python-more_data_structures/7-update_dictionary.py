#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary
    
    Args:
        a_dictionary: the dictionary to modify
        key: the key to add or update (always a string)
        value: the value to set (any type)
        
    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
