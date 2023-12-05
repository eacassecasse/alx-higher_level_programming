#!/usr/bin/python3
"""A BaseGeometry Class."""


class BaseGeometry:
    """Represent the basic geometric figure."""

    def area(self):
        """To be implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a parameter is integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value of the parameter.
        Raises:
            TypeError: If value is not integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
