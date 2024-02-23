# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:35:18 2020

@author: salam_000
"""

ages = {
        'Dick': 51
        }

# The bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'
print('Dick is %s years old' % age)
    
# The good way
age = ages.get('Dick', 'Unknown')
print('Dick is %s yeras old' % age)