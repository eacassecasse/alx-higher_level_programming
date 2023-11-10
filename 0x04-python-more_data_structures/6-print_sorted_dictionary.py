#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    ks = list(a_dictionary.keys())
    ks.sort()
    for k in ks:
        print("{}: {}".format(k, a_dictionary[k]))
