# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:39:10 2020

@author: salam_000
"""

needle = 'f'
haystack = ['a', 'b', 'c', 'd']

# The bad way
"""
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print('Not found')
"""
# The good way
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else: # no break occured
    print('Not found:')