#!/usr/bin/python3
"""A function that write a files content."""


def write_file(filename="", text=""):
    """Write text inside a file."""
    with open(file=filename, mode="w", encoding="UTF-8") as fw:
        return (fw.write(text))
