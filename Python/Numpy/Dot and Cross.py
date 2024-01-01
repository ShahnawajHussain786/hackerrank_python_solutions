# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:54:19 2024

@author: Shahnawaj Hussain
"""

import numpy as np

n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr1.append(temp)
np_arr1 = np.array(arr1)
for j in range(n):
    temp = list(map(int, input().split()))
    arr2.append(temp)
np_arr2 = np.array(arr2)
print(np.dot(np_arr1, np_arr2))

