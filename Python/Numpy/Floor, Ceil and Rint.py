# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:43:25 2024

@author: Shahnawaj Hussain
"""

import numpy as np

np.set_printoptions(legacy="1.13")
A = np.array(input().split(), float)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))