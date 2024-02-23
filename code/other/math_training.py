# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:57:44 2019

@author: salam_000
"""
#Fizz Buzz

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        