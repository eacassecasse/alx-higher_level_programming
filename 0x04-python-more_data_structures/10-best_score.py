#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        mlist = list(a_dictionary.keys())
        scr = 0
        ldr = ""
        for i in mlist:
            if a_dictionary[i] > scr:
                scr = a_dictionary[i]
                ldr = i
        return ldr
