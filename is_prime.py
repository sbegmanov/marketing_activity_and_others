# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:51:52 2020

@author: salam_000
"""

import time
import math
"""
# The bad way
def is_prime_v1(n):
    
    if n == 1:
        return False # 1 is not prime
    
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

## ===== Time Function ====
t0 = time.time()
for n in range(1, 10000):
    is_prime_v1(n)
t1 = time.time()
print("Time required:", t1 - t0)
"""

# The good way
"""
def is_prime_v2(n):
    ' Return 'True' if 'n' is a prime number. False otherwise.'
    if n == 1:
        return False # 1 is not prime
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
        return True
 
t0 = time.time()
for n in range(1, 10000):
    print(is_prime_v2(n))
t1 = time.time()
print("Time required:", t1 - t0)
"""

# The better way
def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    # If it's even and not 2, then it is not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range (3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
        return True

t0 = time.time()
for n in range(1, 10000):
    is_prime_v3(n)
t1 = time.time()
print("Time required:", t1 - t0)