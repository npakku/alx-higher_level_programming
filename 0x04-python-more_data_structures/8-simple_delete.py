#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''delete key from dictionary'''
    if key in a_dictionary.copy():
        del a_dictionary[key]
    return (a_dictionary)
