# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:06:58 2020

@author: salam_000
"""

import logging
import math

# Create and configure logger

LOG_FORMAT = "%(LevelLname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\Lumberjack.log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

logger = logging.getLogger()


def quadratic_formula(a, b, c):
    """ Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))
    
    # Compute the discriminant 
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c
    
    # Compute the two roots
    logger.debug("# Compute the roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b + math.sqrt(disc)) / (2*a)
    
    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)