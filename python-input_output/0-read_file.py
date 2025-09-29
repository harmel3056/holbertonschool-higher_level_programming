#!/usr/bin/python3
"""
Reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
    name of the file to read

    Return:
    Prints the contents of the file as a string
    """
    with open(filename, "r", encoding="UTF-8") as f:
        data = f.read()
    print(f"{data}", end="")
#    print(len(data))


if __name__ == "__main__":
    read_file("my_file_0.txt")
