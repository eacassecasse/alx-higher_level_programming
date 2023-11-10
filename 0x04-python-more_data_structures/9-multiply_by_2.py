#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    ndict = {}
    for k, val in a_dictionary.items():
        ndict.update({k: (val * 2)})
    return ndict
