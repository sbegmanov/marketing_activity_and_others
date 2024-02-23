# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:45:22 2020

@author: salam_000
"""

class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1

s1 = Student()
s2 = Student()
print("The number of students:", Student.count)