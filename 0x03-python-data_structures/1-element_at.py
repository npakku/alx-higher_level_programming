#!/usr/bin/python4

def element_at(my_list, idx):
    '''retrieve element from given index'''

    for i in range(len(my_list)):
        if idx < 0 or idx > len(my_list):
            return None

        elif i == idx:
            found_at = my_list[i]

    return found_at
