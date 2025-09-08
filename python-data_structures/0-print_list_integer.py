#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))

# could do this without .format sans-constraints
#    for item in my_list:
#        print(item)
