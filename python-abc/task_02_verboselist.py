#!/usr/bin/python3
"""
This method would be good for testing. Essentially we extend the
functionality of each of the contained functions to print out the
steps that have been completed as they are completed
"""


class VerboseList(list):
    """
    Inherits from list and extends functionality of a selection
    of functions by printing for each occurrence
    """
    def append(self, item):
        """
        Adds a print line to the append function
        """
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, qty):
        """
        Adds a print line to the extend function
        """
        super().extend(qty)
        print("Extended the list with {} items.".format(len(qty)))

    def remove(self, item):
        """
        Adds a print line to the remove function
        """
        super().remove(item)
        print("Removed {} from the list.".format(item))

    def pop(self, index=-1):
        """
        Adds a print line to the pop function
        """
        item = super().pop(index)
        print("Popped {} from the list.".format(item))
        return item
