# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:10:56 2020

@author: salam_000
"""

class Employee:
    __count = 0;
    def __init__(self):
        Employee.__count = Employee.__count + 1
        
    def display(self):
        print("The number of employee", Employee.__count)
        
emp = Employee()
emp2 = Employee()
emp3 = Employee()

try:
    print("Counting...")
finally:
    emp.display()