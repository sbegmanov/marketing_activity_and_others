# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:54:56 2020

@author: salam_000
"""

    
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
        
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    
@decorator_function
def display():
    print('display function ran')
    

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))
    
display_info('John', 25)
display()