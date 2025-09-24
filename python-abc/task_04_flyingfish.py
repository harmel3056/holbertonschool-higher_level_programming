#!/usr/bin/python3
"""
Demonstration of Method Resolution Order, multiple
inheritance, and the overwrite method of extending
the method of a class. If you rearrange Fish and Bird
in FlyingFish you will achieve different results thanks
to the MRO.
"""


class Fish:
    """
    A concrete class defining two methods
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    A concrete class defining two methods
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A concrete class inheriting from multiple classes and
    overwriting to extend their methods

    Args:
    Fish and Bird classes - inheritance

    Return:
    Prints corresponding statement
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == '__main__':
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
