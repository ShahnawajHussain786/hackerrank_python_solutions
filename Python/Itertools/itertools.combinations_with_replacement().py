# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:57:07 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().split()

result = list(combinations_with_replacement(sorted(s), int(k)))

for item in result:
    print("".join(item))
