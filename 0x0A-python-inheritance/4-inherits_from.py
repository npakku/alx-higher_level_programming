#!/usr/bin/python3

def inherits_from(obj, a_class):
    """python3 -c 'print(__import__("4-inherits_from").inherits_from.__doc__)
    Checks if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
