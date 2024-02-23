# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:19:01 2020

@author: salam_000
"""

import numpy as np
import scipy.optimize as sco

def myFunction(z):
    x = z[0]
    y = z[1]
    w = z[2]
    
    F = np.empty((3))
    F[0] = pow(x, 2) + pow(y, 2) - 20
    F[1] = y - pow(x, 2) 
    F[2] = w + 5 - x*y
    
    return F

zGuess = np.array([1, 1, 1])

z = sco.fsolve(myFunction, zGuess)

print(z)