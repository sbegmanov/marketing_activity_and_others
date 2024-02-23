# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:54:30 2020

@author: salam_000
"""
"""
def __setattr__(self, name, value):
    self.name = value
    
    # since every time an attribute is assigned, __setattr__() is called, this
    # is recursion.
    # so this really means self.__setattr__('name', value). Since the method
    # keeps calling itself, the recurssion goes on forever causing a crash.

def __setattr__(self, name, value):
    self.__dict__[name] = value #assigning to the direct of names in the class
    # define custom behavior here """
    
class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

foo = MyClass(2)
bar = MyClass(3)

print(MyClass.__dict__)
print(foo.__dict__)
print(bar.__dict__)