#!/usr/bin/python3

def raise_exception():
    x = 10
    y = "yes?"
    try:
        print(x / y)
    except TypeError:
        print("Exception raised")
