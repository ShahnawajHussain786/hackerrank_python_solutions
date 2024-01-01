# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:52:01 2024

@author: Shahnawaj Hussain
"""

import numpy as np

n, m = map(int, input().split())
l = []
for i in range(n):
    temp = list(map(int, input().split()))
    l.append(temp)
np_arr = np.array(l)
print(np.mean(np_arr, axis=1))
print(np.var(np_arr, axis=0))
print(round(np.std(np_arr, axis=None), 11))