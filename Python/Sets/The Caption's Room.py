# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:42:26 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = list(input().split())
shahnawaj = set()
nawaj = set()
for i in rooms:
    if i in shahnawaj:
        nawaj.add(i)
    else:
        shahnawaj.add(i)
print(''.join(shahnawaj.difference(nawaj)))
