# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:10:44 2020

@author: salam_000
"""

class Building(object):
    def __init__(self, floors):
        self._floors = [None]*floors
    def occupy(self, floor_number, data):
        self._floors[floor_number] = data
    def get_floor_data(self, floor_number):
        return self._floors[floor_number]
    
building1 = Building(4)
building1.occupy(0, 'Reception')
building1.occupy(1, 'ABC Corp')
building1.occupy(2, 'DEF Inc')

print(building1.get_floor_data(2)) 

"""With getitem, setitem """
class Building(object):
    def __init__(self, floors):
        self._floors = [None]*floors
    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data
    def __getitem__(self, floor_number):
        return self._floors[floor_number]

building1 = Building(4)
building1[0] = 'Recepton'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print(building1[2])