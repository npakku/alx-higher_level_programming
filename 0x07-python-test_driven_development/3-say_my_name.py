#!/usr/bin/python3

"""Defines a function that says name

   python3 -c 'print(__import__("3-say_my_name").__doc__)'
"""

def say_my_name(first_name, last_name=""):
    """says a name
    python3 -c 'print(__import__("my_module").say_my_name.__doc__)'
    Args:
        first_name(str): the first name to print
        last_name(str): the last name to print

    Raises:
        TypeError if either first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("First name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("Last name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
