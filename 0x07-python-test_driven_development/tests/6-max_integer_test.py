#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This module defines unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered_list = [1, 2, 3]
        self.assertEqual(max_integer(ordered_list), 3)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered_list = [1, 4, 2]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [15.53, 68.9, -4.61, 9.2, 90.4]
        self.assertEqual(max_integer(floats), 90.4)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [15.53, 68.9, -150, 75, 31]
        self.assertEqual(max_integer(ints_and_floats), 75)

    def test_string(self):
        """Test a string."""
        string = "Ezra"
        self.assertEqual(max_integer(string), 'z')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Ezra", "is", "my", "colleague"]
        self.assertEqual(max_integer(strings), "my")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
