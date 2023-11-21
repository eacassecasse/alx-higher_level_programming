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

    @property
    def size(self):
        """Getter for size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size property"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """Compute and return area of a square"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
                
