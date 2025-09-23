#!/usr/bin/python3
"""
Returns True for an object that is either the type identified
or is an inherited instance of the type identified
"""


def is_kind_of_class(obj, a_class):
    """
    Identifies if an object is part of a class family

    Args:
    obj - object to identify type family

    Return:
    True if object is an instance of, or if the object
    is an instance of a class that inherited from, the
    specified class. Otherwise False.
    """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False

# Note that this is a super C way of writing this:
# isinstance already returns a boolean (True or False) so you
# could simply have passed:
# return isinstance(obj, a_class)
# into the function