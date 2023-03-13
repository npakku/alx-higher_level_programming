#!/usr/bin/python3
#Author: Pascal<pascal.naa.zury@gmail.com>

def print_reversed_list_integer(my_list=[]):
    '''print list in reverse order'''
    
    rev = []
    for i in range(-1, -6, -1):
        rev.append(my_list[i])

    for i in range(len(rev)):
        print("{}".format(rev[i]))
  
