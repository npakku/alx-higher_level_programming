#!/usr/bin/python3
def no_c(my_string):
    copy = [character for character in \
            my_string if character != 'c' and character != 'C']
    return ("".join(copy))
