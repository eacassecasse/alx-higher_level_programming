#!/usr/bin/python3
"""A function that write a files content."""


def append_write(filename="", text=""):
    """Appends text inside a file."""
    with open(file=filename, mode="a", encoding="UTF-8") as fw:
        return (fw.write(text))