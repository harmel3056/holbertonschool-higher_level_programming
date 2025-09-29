#!/usr/bin/python3
"""
Appends text to an existing file, or creates
the file and adds the text if it doesn't exist
"""


def append_write(filename="", text=""):
    """
    Appends text to a file

    Args:
    filename - name of the file to add or update
    text - contents to add to the file

    Return:
    text is added to the file
    number of characters added is returned
    """
    with open(filename, "a", encoding="UTF-8") as f:
        data = f.write(text)
    return data


if __name__ == "__main__":
    append_write = __import__('2-append_write').append_write

    nb_chars_add = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_chars_add)
