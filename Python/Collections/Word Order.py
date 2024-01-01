# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:39:11 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


word_ar = []
n = int(input())
for i in range(n):
    word_ar.append(input().strip())
word_counter = OrderedCounter(word_ar)
print(len(word_counter))
for word in word_counter:
    print(word_counter[word], end=" ")
