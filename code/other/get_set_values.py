# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:27:59 2020

@author: salam
"""


class InstanceCounter(object):
    count = 0
    
    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1
    
    def set_val(self, newval):
        self.val = newval
        
    def get_val(self):
        return self.val
    
    def get_count(self):
        return InstanceCounter.count
    
a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print("value of obj: %s" % (obj.get_val))
    print("count: %s" % (obj.get_count()))