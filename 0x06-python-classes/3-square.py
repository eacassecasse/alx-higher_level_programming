#!/usr/bin/python3

class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes the Square."""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute and return area of a square"""
        return self.__size**2
