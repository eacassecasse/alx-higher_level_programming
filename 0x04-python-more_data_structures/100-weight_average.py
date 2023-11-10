#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    _sum = 0
    size = 0

    for tup in my_list:
        _sum += tup[0] * tup[1]
        size += tup[1]

    return (_sum / size)
