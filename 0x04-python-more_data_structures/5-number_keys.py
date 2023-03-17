#!/usr/bin/python3

def number_keys(a_dictionary):
    '''count number of keys in a dictionary'''
    my_list = []
    for k, v in a_dictionary.items():
        my_list.append(k)

    return (len(my_list))
