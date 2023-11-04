#!/usr/bin/python3

def uppercase(str):
    for o in str:
        if ord(o) >= 97 and ord(o) <= 122:
            o = chr(ord(o) - 32)

        print("{}".format(o), end="")

    print("")
