# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:31:39 2024

@author: Shahnawaj Hussain
"""

import numpy
array = list(map(int, input().split()))
np_arr = numpy.array(array)
print(numpy.reshape(np_arr, (3, 3)))

