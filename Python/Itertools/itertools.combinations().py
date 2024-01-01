# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:55:00 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
word , l = input().split()
for i in range(1, int(l)+1):
    for j in combinations(sorted(word), i):
        print (''.join(j))