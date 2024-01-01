# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:59:57 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
myset_a = set(map(int, input().split()))
n2 = int(input())
myset_b = set(map(int, input().split()))
a = (myset_a.difference(myset_b))
b = (myset_b.difference(myset_a))
ans = a.union(b)
for i in sorted(ans):
    print(i)
