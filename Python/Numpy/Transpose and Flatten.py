# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:33:38 2024

@author: Shahnawaj Hussain
"""

import numpy

n, m = map(int, input().split())
l = []
for i in range(n):
    r = list(map(int, input().split()))
    l.append(r)

np_arr = numpy.array(l)
print(numpy.transpose(np_arr))
print(np_arr.flatten())