# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:28:51 2020

@author: salam_000
"""

def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

for c in range(0, 100):
    print(fibonacci(c))
    
