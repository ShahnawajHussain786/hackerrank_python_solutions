# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:56:17 2024

@author: Shahnawaj Hussain
"""

import numpy as np

np_ar1 = np.array(list(map(int, input().split())))
np_ar2 = np.array(list(map(int, input().split())))
print(np.inner(np_ar1, np_ar2))
print(np.outer(np_ar1, np_ar2))