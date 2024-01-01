# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:48:04 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
shahnawaj = set(input().split())
N = int(input())

for _ in range(N):
    nawaj = set(input().split())
    if nawaj - shahnawaj:
        print(False)
        break
        
else:
    print(True)