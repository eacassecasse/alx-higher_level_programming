#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """A representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a representation of a Student in JSON format."""
        return self.__dict__
