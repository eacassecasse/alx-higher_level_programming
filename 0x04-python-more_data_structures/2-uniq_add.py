#!/usr/bin/python3


def uniq_add(my_list=[]):
    nlist = []
    sum = 0
    for n in my_list:
        if n not in nlist:
            sum += n
            nlist.append(n)
    return sum
