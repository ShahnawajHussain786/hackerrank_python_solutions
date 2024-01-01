# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:02:08 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
marks = []
for _ in range(X):
    marks.append(list(map(float, input().split())))
for i in zip(*marks):
    print(sum(i) / len(i))