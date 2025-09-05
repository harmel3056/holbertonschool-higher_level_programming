#!/usr/bin/python3
import sys


def add_args(*argv):
    int_args = [int(arg) for arg in argv]
    print(sum(int_args))


if __name__ == "__main__":
    add_args(*sys.argv[1:])
