# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:44:58 2020

@author: salam_000
"""

import numpy as np
from scipy import interpolate
import pylab as py

def func(x, y):
    return (x+y)*np.exp(-5.0*(x**2 + y**2))

x = np.random.uniform(-1.0, 1.0, size=50)
y = np.random.uniform(-1.0, 1.0, size=50)
fvals = func(x, y)
newfunc = interpolate.Rbf(x, y, fvals, function='multiquadric')
xnew, ynew = np.mgrid[-1:1:100j, -1:1:100j]
fnew = newfunc(xnew, ynew)
tru = func(xnew, ynew)

# Create image plot
py.figure(1)
py.clf()
py.imshow(fnew, extent=[-1, 1, -1, 1], cmap=py.cm.jet)
py.scatter(x, y, 30, fvals, cmap=py.cm.jet)

# Create surface plot
from enthought.mayavi import mlab

mlab.clf()
mlab.surf(xnew, ynew, fnew*2)