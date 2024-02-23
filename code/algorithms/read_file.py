# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:56:17 2020

@author: salam_000
"""
"""
# The bad way
f = open('F:\python_algorithms\pimp.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()
"""

# The better way
with open ('F:\python_algorithms\pimp.txt') as f:
    for line in f:
        print(line)
        
