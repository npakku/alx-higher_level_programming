#!/usr/bin/python3

'''my class that inherits list'''

class MyList(list):
    '''implement the inherited class list'''
    
    def print_sorted(self):
	'''print list in sorted order'''
	print(sorted(self))
	
