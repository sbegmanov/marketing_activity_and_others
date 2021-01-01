# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:05:33 2020

@author: salam_000
"""
from functools import wraps

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info(
                'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    
    return wrapper

def my_timer(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    
    return wrapper

# =============================================================================
# @decorator_function
# def display():
#     print('display function ran')
# =============================================================================
import time
    
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display info ran with arguments ({}, {})'.format(name, age))

display_info = my_timer(display_info)
print(display_info.__name__)    
display_info('John', 25)
#display()
        