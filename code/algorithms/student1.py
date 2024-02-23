# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:52:13 2020

@author: salam_000
"""

class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        
# create the object of the class Student
s = Student("John", 101, 22)
print(s)

# prints the attribute name of the object s
print(getattr(s, 'name'))

# reset the value of attribute age to 23
setattr(s, "age", 23)

# print modified value of the age
print(getattr(s, 'age'))

# prints true if the student contains the attribute with name id

print(hasattr(s, 'id'))
# deletes the attribute age
delattr(s, 'age')

# this will give an error since the attribute age deleted
print(s.age)
        