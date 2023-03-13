#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, new_element):
    '''replace element at an index'''
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = new_element
    return (my_list)
