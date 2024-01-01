# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:50:11 2024

@author: Shahnawaj Hussain
"""

import numpy
n, m = map(int, input().split())
l = []
for i in range(n):
    t = list(map(int, input().split()))
    l.append(t)
np_array = numpy.array(l)
print(numpy.max(numpy.min(np_array, axis=1)))