# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:34:04 2020

@author: salam
"""


from functools import reduce

# Multiply all numbers in a list

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y

z = reduce(multiplier, data)
print(z)

# same as above

product = 1

for x in data:
    product = product * x

print(product)