#!/usr/bin/python3
"""A function that reads a files content."""


def read_file(filename=""):
    """Read all the content of a text file."""
    with open(file=filename, mode="r", encoding="UTF-8") as fr:
        print(fr.read())
