#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides elements of 2 lists, 
    each with its own correspondant.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A list containing all the divisions.
    """
    nlist = []
    for i in range(0, list_length):
        try:
            q = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            q = 0
        except ZeroDivisionError:
            print("division by 0")
            q = 0
        except IndexError:
            print("out of range")
            q = 0
        finally:
            nlist.append(q)
    return (nlist)
