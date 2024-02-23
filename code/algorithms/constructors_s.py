# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:36:48 2020

@author: salam_000
"""
"""
class Vehicle:
    def __init__(self, color_choice = "White"):
        self.color = color_choice
    def show_color(self):
        return self.color
    
my_v = Vehicle()
your_v = Vehicle("Red")

print(my_v.show_color())
print(your_v.show_color())
"""
class Vehicles(object):
    max_objects = 2
    curr_objects = 0
    
    def __new__(cls):
        if (cls.curr_objects >= cls.max_objects):
            raise ValueError("Cannot create more objects")
        cls.curr_objects += 1
        return super().__new__(cls)
    
print(Vehicles())
print(Vehicles())
print(Vehicles())


