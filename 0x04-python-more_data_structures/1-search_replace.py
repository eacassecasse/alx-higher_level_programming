#!/usr/bin/python3


def search_replace(my_list, search, replace):
    nlist = []
    for el in my_list:
        if el == search:
            nlist.append(replace)
        else:
            nlist.append(el)
    return nlist
