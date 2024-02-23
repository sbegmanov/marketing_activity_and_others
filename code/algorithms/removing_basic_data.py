# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:18:39 2020

@author: salam
"""

# Remove missing data

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Columbia", 
             "", "Ecuador", "", "", "Venezuela"]

y = list(filter(None, countries))

print(y)