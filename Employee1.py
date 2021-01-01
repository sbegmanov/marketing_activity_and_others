# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:37:34 2020

@author: salam_000
"""

class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + '@gmail.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def aplly_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        


    def __repr__(self):
          return "Employee('{}', '{}', {})".format(self.first, self.last, 
                                                   self.pay)
      
    def __str__(self):
          return '{} - {}'.format(self.fullname(), self.email)
   
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)
 
print(emp_1)
print(str(emp_1))

print(len(emp_1))

print(len('test')) 
print('test'.__len__())
# =============================================================================
# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))
# =============================================================================
