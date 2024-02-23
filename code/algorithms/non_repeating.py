# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:29:15 2020

@author: salam
"""


"""
Non repeat element
Take a string and return character that never repeats
if multiple uniques then return only the first unique

"""
# =============================================================================
# def non_repeating(s):
#     s = s.replace(' ', '').lower()
#     char_count = {}
#     
#     for c in s:
#         if c in char_count:
#             char_count[c] += 1
#         else:
#             char_count[c] = 1
#     
#     for c in s:
#         if char_count[c] == 1:
#             return c
#     return None
# 
# print(non_repeating('I Apple Ape Peels'))
# =============================================================================

########################################################

def non_repeating(s):
    s = s.replace(' ', '').lower()
    char_count = {}
    
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    
    all_uniques = []
    y = sorted(char_count.items(), key=lambda x: x[1]) # print(y)
        # y = sorted(x(1, 1, 2, 2, 4, 4))
        # [('i', 1), ('s', 1), ('a', 2), ('l', 2), ('p', 4), ('e', 4)]
 
    for item in y:
        if item[1] == y[0][1]:  #  [0][1] = 1
            all_uniques.append(item)
    return all_uniques   # replace with 'y'

print(non_repeating('I Apple Ape Peels'))

# To get deep understanding

# =============================================================================
# char_count = {'i': 1, 'a': 2, 'p': 4, 'l': 2, 'e': 4, 's': 1}
# 
# y = sorted(char_count.items(), key=lambda x: x[1])
# print(y)
# =============================================================================

# =============================================================================
# def non_repeating(s):
#     s = s.replace(' ', '').lower()
#     char_count = {}
#     
#     for c in s:
#         if c in char_count:
#             char_count[c] += 1
#         else:
#             char_count[c] = 1
#     
#     return char_count
# 
# print(non_repeating('I Apple Ape Peels'))
# =============================================================================
# =============================================================================
# char_count = {'i': 1, 'a': 2, 'p': 4, 'l': 2, 'e': 4, 's': 1}
# 
# # y = sorted(char_count.items(), key=lambda x: x[1])
# 
# y = char_count.items()
# print(y)
# =============================================================================
