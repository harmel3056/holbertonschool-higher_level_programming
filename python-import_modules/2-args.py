#!/usr/bin/python3
def print_args(*argv):
    if len(argv) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv)), end="\n")
        j = 1
        for i in range(len(argv)):
            print("{}: {}".format(j, argv[i]), end="\n")
            j += 1
