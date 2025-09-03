#!/usr/bin/python3
for i in range(00, 100):
    if i < 10:
        print(f"0{i}", end=", ")
    else:
        print(f"{i}", end=", " if i != 99 else "\n")
