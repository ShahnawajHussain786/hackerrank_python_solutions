# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:53:18 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOU
from itertools import permutations
word,length = input().split()

list = ["".join(pair) for pair in permutations(word, int(length))]
for i in sorted(list):
    print(i)