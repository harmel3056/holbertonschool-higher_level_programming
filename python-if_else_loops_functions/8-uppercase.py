#!/usr/bin/python3
def uppercase(string):
    upper_string = []
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        upper_string.append(upper_char)
    print("{}".format("".join(upper_string)))
