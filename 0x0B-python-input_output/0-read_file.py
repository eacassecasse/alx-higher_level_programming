#!/usr/bin/python3
"""A function that reads a files content."""


def read_file(filename=""):
    """Read all the content of a text file encoded in UTF-8."""
    with open(file=filename, mode="r", encoding="UTF-8") as fr:
        print(fr.read(), end="")
