#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    Args:
        my_list_1: First list (can contain any type)
        my_list_2: Second list (can contain any type)
        list_length: Length of the new list

    Returns:
        A new list (length = list_length) with all divisions
    """
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                value = 0
            else:
                value = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            value = 0
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        finally:
            result.append(value)
    return result
