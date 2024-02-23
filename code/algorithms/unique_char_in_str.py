# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:30:58 2020

@author: salam
"""

"""
Given a string, are all characters unique?
Should give a True or False at return
Uses Python built-in structures
"""
# A set is a collection which is unordered and unindexed
# A set checks for the unique values
def unique(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string) # try  print(set(string))
    
print(unique('i lkj rejw'))

#############

def unique(s):
    s = s.replace(' ', '')
    characters = set()
    
    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True

#print(unique('a b cdef'))
print(unique('i lkj rejw'))
