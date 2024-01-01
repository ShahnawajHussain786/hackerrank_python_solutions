# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:59:16 2024

@author: Shahnawaj Hussain
"""

import numpy as np

np.set_printoptions(legacy="1.13")
n = int(input())
array = np.array([input().split() for i in range(n)], float)
print(np.linalg.det(array))
