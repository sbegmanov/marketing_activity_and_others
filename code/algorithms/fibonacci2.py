# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:52:18 2020

@author: salam_000
"""

def fibonacci():
    
    a, b = 0, 1
    while True:
        yield a
        print(a) 
        a, b = b, a + b
               
        
