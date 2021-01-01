# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:59:37 2020

@author: salam_000
"""

import time as _time
import math as _math

def _cmp(x, y):
    return 0 if x == y else 1 if  x > y else -1

MINYEAR = 1
MAXYEAR = 9999
_MAXORDINAL = 3652059 # date.max.toordinal()


@property
def microseconds(self):
    """microsends"""
    return self._microseconds
