#!/usr/bin/python3
"""An inherited class of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square based on rectangle."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """print() and str() representation of a Square."""
        string = super(self).__str__()
        string += str(self.__size) + "/" + str(self.__size)
        return string
