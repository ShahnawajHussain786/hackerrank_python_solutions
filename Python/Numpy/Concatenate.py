# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:35:11 2024

@author: Shahnawaj Hussain
"""

import numpy

n, m, p = map(int, input().split())

l1 = []
l2 = []
for i in range(n):
    temp = list(map(int, input().split()))
    l1.append(temp)
for j in range(m):
    temp = list(map(int, input().split()))
    l2.append(temp)
np_arr1 = numpy.array(l1)
np_arr2 = numpy.array(l2)
print(numpy.concatenate((np_arr1, np_arr2), axis=0))