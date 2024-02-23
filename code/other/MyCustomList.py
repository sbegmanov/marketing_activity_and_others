# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:43:38 2020

@author: salam_000
"""

class MyCustomList(list):
    
    def __getitem__(self, index):
        if index == 0:
            raise ValueError
        index = index - 1
        return list.__getitem__(self, index)
    
    def __setitem__(self, index, value):
        if index == 0:
            raise ValueError
        index = index - 1
        return list.__setitem__(self, index, value)
    
    def __delitem__(self, key):
        key = key - 1
        return list.__delitem__(self, key)
    
    def __mul__(self, other):
        mul_list = [x * y for x, y in zip(self, other)]
        return MyCustomList(mul_list)
    
list_one = MyCustomList([1, 2, 3, 4, 5])
