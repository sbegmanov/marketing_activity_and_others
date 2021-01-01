# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:19:59 2020

@author: salam
"""


"""
Common Elements in Two Sorted Arrays
return the common elements (as an array) between two sorted arrays of integers
(ascending order).
Example: The commone elements between [1, 3, 4, 6, 7, 9] and 
[1, 2, 4, 5, 9, 10] are [1, 4, 9, ]
"""

def common_elements(a, b):
    p1 = 0
    p2 = 0
    
    result = []
    
    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 += 1
            p2 += 1
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1
    return result

print(common_elements([1, 3, 4, 6, 7, 10, 11, 12], [1, 2, 4, 5, 9, 10]))