# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:51:04 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = input().split()
b = input().split()
c = [int(a[i])for i in range(len(a))]
d = [int(b[j]) for j in range(len(b))]

print(*list(product(c,d)))
