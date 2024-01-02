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

    def to_json(self, attrs=None):
        """Return a representation of a Student in JSON format.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {f: getattr(self, f) for f in attrs if hasattr(self, f)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student with
        those provided in the JSON argument.

        Args:
            json (dict): The key/value pairs to replace attrs with.
        """
        for key, value in json.items():
            setattr(self, key, value)
