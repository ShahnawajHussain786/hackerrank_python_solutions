# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:00:44 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
a = input().split()
k = int(input())
l1 = list(combinations(a, k))
l2 = [e for e in l1 if "a" in e]
P = len(l2) / len(l1)
print('%.4f' % P)