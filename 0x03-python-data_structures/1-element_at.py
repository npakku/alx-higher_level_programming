#!/usr/bin/python4

def element_at(my_list, idx):
    '''retrieve element from given index'''

    for i in range(len(my_list)):
        if idx < 0 or idx > len(my_list) - 1:
            return None

    return my_list[idx]
