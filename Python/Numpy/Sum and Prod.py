# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:46:43 2024

@author: Shahnawaj Hussain
"""

import numpy as np

n, m = map(int, input().split())
l = []
for i in range(n):
    temp = list(map(int, input().split()))
    l.append(temp)
np_arr = np.array(l)
s = np.sum(np_arr, axis=0)
print(np.prod(s))