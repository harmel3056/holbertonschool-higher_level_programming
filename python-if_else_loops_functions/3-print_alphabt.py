#!/usr/bin/python3
ranges = (range(97, 101), range(102, 113), range(114, 123))
output = [num for i in ranges for num in i]
ascii_output = ''.join(chr(num) for num in output)
print(f"{ascii_output}", end="")
