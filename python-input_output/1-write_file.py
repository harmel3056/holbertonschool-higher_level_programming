#!/usr/bin/python3
"""
Writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
    filename - name of the file to be written to
    text - text to write to the file

    Return:
    the text is applied to the file as an overwrite
    the number of chars in the string written is returned
    """
    with open(filename, "w", encoding="UTF-8") as f:
        data = f.write(text)
    return data


if __name__ == "__main__":
    nb_chars = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_chars)
