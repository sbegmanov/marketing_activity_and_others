# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:03:31 2020

@author: salam_000
"""

x = 10
y = -10

# good way to write
x, y = 10, -10

print('Before: x = %d, y = %d' %(x, y))

# The bad way
tmp = y
y = x
x = tmp

print('After: x = %d, y = %d' %(x, y))

# The good way
x, y = y, x
print('After: x = %d, y = %d' %(x, y))
