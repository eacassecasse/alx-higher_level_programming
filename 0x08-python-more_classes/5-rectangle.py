#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the current width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the current height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Computes and return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self) -> str:
        """Return the official rectangle representation
        for end-user with the # character."""
        res = ""

        if self.__width != 0 and self.__height != 0:
            for i in range(0, self.__height):
                res += "#" * self.__width

                if i < self.__height - 1:
                    res += "\n"

        return res

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
