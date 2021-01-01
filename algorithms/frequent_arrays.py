# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:59:46 2020

@author: salam
"""

def most_frequent(list):
    count = {}
    max_count = 0            # try to remove
    max_item = None          # try to remove
    
    for i in list:
        if i not in count:
            count[i] = 1
        else:                        # try to remove
            count[i] += 1            # try to remove
        
        if count[i] > max_count:    # try to remove
            max_count = count[i]    # try to remove
            max_item = i            # try to remove
    return max_item                 # put count to check dictionary

#print(most_frequent([1, 3, 3, 4, 2, 1, 1]))
print(most_frequent([-1, 3, 3, 4, 2, -1, -1]))
