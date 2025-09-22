#!/usr/bin/python3
"""
Essentially builds a new class using the [inbuilt] methods of list,
however by building upon that with our own methods we can
create a class that is custom to our needs.
"""


class MyList(list):
    """
    Class that inherits from list and prints sorted input values

    Args:
    list - takes mathods from this inbuilt class

    Return:
    printed copy of the entered integer list
    """
    def print_sorted(self):
        print(sorted(self))
