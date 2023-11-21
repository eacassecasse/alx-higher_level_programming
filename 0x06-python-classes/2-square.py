#!/usr/bin/python3

"""Definition a Square class"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes the Square."""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
