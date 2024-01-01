# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:02:33 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k, m = map(int, input().split())

a0 = []
for i in range(k):
    a1 = list(map(int, input().split()))
    a0.append(a1[1:])

combinations = itertools.product(*a0)
result = 0
for combination in combinations:
    result = max(sum(x * x for x in combination) % m, result)
print(result)
