# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:14:45 2020

@author: salam
"""


import math

def area(r):
    """ Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)
# print(areas)

# Method 2: Use 'map' function

y = map(area, radii)

print(list(y))
