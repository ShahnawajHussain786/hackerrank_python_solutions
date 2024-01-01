# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:36:43 2024

@author: Shahnawaj Hussain
"""

import numpy

n = tuple(map(int, input().strip().split()))
print(numpy.zeros(n, dtype=numpy.int32))
print(numpy.ones(n, dtype=numpy.int32))
