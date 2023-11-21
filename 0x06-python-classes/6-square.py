#!/usr/bin/python3

class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0,0)):
        """Initializes the Square."""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not type(position) is tuple or 
                len(position) != 2 or
                not all([isinstance(el, int) for el in position]) or 
                not all(el>=0 for el in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        """Getter for position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position property"""
        if (not type(value) is tuple or 
                len(value) != 2 or
                not all([isinstance(el, int) for el in value]) or
                not all(el>=0 for el in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """Compute and return area of a square"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        else:
            for _ in range(0, self.__size):
                print(" " * self.__position[0] if self.__position[1] <= 0 else "", end="")
                print("#" * self.__size)
                
