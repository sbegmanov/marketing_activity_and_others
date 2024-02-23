# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:09:13 2020

@author: salam_000
"""

def reverse(x):
    return x[:: -1]
text = input()

if __name__ == "__main__":
    print('Reverse String using slicing =', reverse(text))