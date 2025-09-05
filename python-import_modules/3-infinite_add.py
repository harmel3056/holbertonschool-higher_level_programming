#!/usr/bin/python3
import sys


def add_args():
    args = sys.argv[1:]
    
    int_args = [int(arg) for arg in args]
    print(sum(int_args))


if __name__ == "__main__":
    add_args()
