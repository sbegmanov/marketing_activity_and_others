# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:47:16 2020

@author: salam_000
"""

def anagram2(s1, s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False
    
    # Create counting dictionary (Note could use DefaultDict 
    # Collections module)
    count = {}
    
    # Fill dictionary for first string (add counts)
    for letter in s1: # for ever letter in first string
        if letter in count: # if letter is already in my dictionary
            count[letter] += 1 # add 1 to that letter key
        else:
            count[letter] = 1
            
    # Fill dictionary for second string(subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
   
    # Check that all counts are 0    
    for k in count:
        if count[k] != 0:
            return False
    # Otherwise they're anagrams 
    return True

x  = anagram2('gog', 'xxx')
print(x)