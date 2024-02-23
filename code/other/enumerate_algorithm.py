# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:35:15 2020

@author: salam_000
"""

cities = ['Marseille', 'Amsterdam', 'New York', 'London']
# The bad way
"""
i=0
for city in cities:
    print(i, city)
    i += 1 
"""
    
# The good way
for i, city in enumerate(cities):
    print(i, city)