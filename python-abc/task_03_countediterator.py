#!/usr/bin/python3
"""
Extends the init and iter inbuilt functions to incorporate
a counter. Function takes a list and returns the items
plus the number of items iterated through
"""


class CountedIterator:
    """
    Takes a list and returns the items plus the number
    of iterations
    """
    def __init__(self, data):
        """
        Sets the iterator and counter attributes

        Args:
        data - input data
        """
        self.iterator = iter(data)
        self.counter = 0

    def __iter__(self):
        """
        Ensures the class can run on a loop (is iterable)
        """
        return self

    def __next__(self):
        """
        Extends the __next__ class with a counter and raises
        StopIteration for end of list
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Returns the final iterator count
        """
        return self.counter


if __name__ == '__main__':
    data = [10, 20, 30, 40]
    ci = CountedIterator(data)

    for item in ci:
        print(item)

    print("Counted iterations:", ci.get_count())

    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, "
                  f"total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
