# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:49:43 2020

@author: salam_000
"""

# Decorators

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')
   
display = decorator_function(display)
print(display)
    