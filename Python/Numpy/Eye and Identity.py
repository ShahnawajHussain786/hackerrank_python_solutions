# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:38:41 2024

@author: Shahnawaj Hussain
"""

import numpy as np

np.set_printoptions(legacy="1.13")
n, m = map(int, input().split())
print(np.eye(n, m, k=0))