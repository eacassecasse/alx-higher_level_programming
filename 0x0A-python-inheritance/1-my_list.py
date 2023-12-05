#!/usr/bin/python3
"""
Defines the MyList class
"""


class MyList(list):
    """This class is a subclass of list"""
    def __init__(self):
        """initializes the list"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
