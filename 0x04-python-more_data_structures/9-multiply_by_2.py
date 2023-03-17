#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''multipy each element of dictionary by 2'''
    for key, value in a_dictionary.items():
        a_dictionary[key] = 2*value
    return a_dictionary
