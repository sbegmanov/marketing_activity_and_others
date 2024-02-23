# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:41:42 2020

@author: salam_000
"""

x_list = [1, 2, 3]
y_list = [2, 4, 6]

# The bad way

"""
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    
    print(x, y)  """
    
# The good way
for x, y in zip(x_list, y_list):
    print(x, y)
    
