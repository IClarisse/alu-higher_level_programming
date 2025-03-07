#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
        my_list: The list containing elements of any type
        x: Number of elements to access in my_list

    Returns:
        The real number of integers printed
    """
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                # Skip non-integer values silently
                continue
    except IndexError:
        # This will be raised if x is greater than the length of my_list
        # We don't handle it here as per requirements, so it propagates
        raise

    print()
    return count
