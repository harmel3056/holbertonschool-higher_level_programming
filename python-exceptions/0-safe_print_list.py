#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        output = ("".join(map(str, my_list[:x])))
        count = 0
        for i in output:
            count += 1
        print(output)
        return count
    except (ValueError, TypeError, AttributeError):
        print("nah mate")
