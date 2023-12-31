#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle.

        Attributes:
            number_of_instances (int): number of rectangles created.
            print_symbol (any): default character to be printed.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and return the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes and return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width) + (2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes and return the biggest area between 2 given rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)

        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Initialize a new square.

        Args:
            size (int): Defines the width and
            height of the square.
        """
        return (cls(size, size))

    def __str__(self) -> str:
        """Return the official rectangle representation
        for end-user with the print_symbol character."""
        if self.__width == 0 and self.__height == 0:
            return ""

        res = []

        for i in range(self.__height):
            [res.append(self.print_symbol) for _ in range(self.__width)]

            if i != self.__height - 1:
                res.append("\n")

        return ("".join(res))

    def __repr__(self):
        """
        Returns a representation of the
        Rectangle instantiation.
        """
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return (ret)

    def __del__(self):
        """Method called before the rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
