# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:38:37 2020

@author: salam_000
"""

class Word(str):
    "Class for words, defining comparison based on word length."
    
    def __new__(cls, word):
        # Note that we have to use __new__. This is because str is an immutable.
        # type, so we have to initialize it early (at creation)
        
        if ' ' in word:
            print("Value contains spaces. Trancuting to first space.")
            word = word[:word.index('')] # Word is now all chars before first space
        return str.__new__(cls, word)
    
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

word_ = Word('sal').__ge__('salik')

print(word_)