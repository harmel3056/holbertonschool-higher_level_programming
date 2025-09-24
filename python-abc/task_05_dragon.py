#!/usr/bin/python3
"""
Explores the use of Mixins as a nice flexible
alternative to strict inheritance hierarchy. Note
that Dragon inherits the mixins but they do not
form part of the core logic
"""


class SwimMixin:
    """
    First optional inclusion for the Dragon class
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Second optional inclusion for the Dragon class
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class that takes two optional mixins and returns
    printed actions

    Args:
    SwimMixin - sends our dragon swimming
    FlyMixin - sends our dragon flying

    Return:
    Printed actions of the dragon
    """
    def roar(self):
        print("The dragon roars!")

    def draco(self):
        self.swim()
        self.fly()
        self.roar()


if __name__ == '__main__':
    dragon = Dragon()
    dragon.swim()  # Outputs: The creature swims!
    dragon.fly()   # Outputs: The creature flies!
    dragon.roar()  # Outputs: The dragon roars!
