# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:56:26 2024

@author: Shahnawaj Hussain
"""

import numpy

p = numpy.array(list(map(float, input().split())), float)
x = float(input())
print(numpy.polyval(p, x))
