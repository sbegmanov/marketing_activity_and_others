# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:51:56 2020

@author: salam
"""


temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 29), 
         ("Berlin", 29), ("Berlin", 29), ("Berlin", 29),
         ("Berlin", 29), ("Berlin", 29)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32) # Like

y = list(map(c_to_f, temps))
print(y)

