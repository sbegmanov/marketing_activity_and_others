# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:38:43 2020

@author: salam_000
"""
"""
# The bad way
print('Converting!')
print(int('4'))
print('Done!')
"""
# The good way
print('Converting...')

try:
    print(int('4'))
except:
    print('Conversion failed!')
else:
    print('Conversion successful!')
finally: #always
    print('Done!')
        