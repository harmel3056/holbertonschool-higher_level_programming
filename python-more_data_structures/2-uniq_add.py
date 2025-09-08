#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    for int in my_list:
        if int not in new_list:
            new_list.append(int)
    return (sum(new_list))
