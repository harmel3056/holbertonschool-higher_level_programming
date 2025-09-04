#!/usr/bin/python3
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]

    if len(argv) == 0:
        print("0 arguments.")
    else:
        if len(argv) == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(argv)), end="\n")
        j = 1
        for i in range(len(argv)):
            print("{}: {}".format(j, argv[i]), end="\n")
            j += 1
