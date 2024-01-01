# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:28:44 2024

@author: Shahnawaj Hussain
"""

import numpy

def arrays(arr):
    # complete this function
    np_arr = numpy.array(arr, dtype=float)
    return(np_arr[::-1])

arr = input().strip().split(' ')
result = arrays(arr)
print(result)