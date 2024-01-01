#!/usr/bin/python3
"""An inherited class of int."""


class MyInt(int):
    """
    A class based on int to invert == & != operators.
    """

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
