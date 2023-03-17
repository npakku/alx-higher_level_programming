#!/usr/bin/python

def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value pairs in a dictionary."""
    #key_list = []
    for keys in a_dictionary.copy():
     #   key_list.append(key)
        if key not in keys:
            a_dictionary[key] = value
    return a_dictionary
