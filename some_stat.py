# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:11:33 2020

@author: salam
"""

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

y =list(filter(lambda x: x > avg, data))

print(y)

x =list(filter(lambda x: x > avg, data))

print(x)