# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:51:54 2020

@author: salam_000
"""

"""
Array pair Sum
Given an integer array, output all the unique pairs that sum up to a special
value k.
So the input:
pair_sum([1, 2, 3, 4])
would return 2 pairs:
    (1, 3)
    (2, 2)
    
"""

def pair_sum(array, k):
    if len(array) < 2:
        return print('Too small')
    
    seen = set()
    output = set()
    
    for num in array:
        target = k - num
        
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
            
    print('\n'.join(map(str, list(output))))
    
pair_sum([1, 3, 2, 2], 4)