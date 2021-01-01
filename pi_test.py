# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:07:54 2020

@author: salam
"""


import unittest
from pi import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_areas(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEquals(circle_area(0), 0)
        self.assertAlmostEquals(circle_area(2.1), pi * 2.1**2)
    
    def test_values(self):
         # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)
    
    def test_types(self):
        # Make sure errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
                           