# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:44:51 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    if len(b - a) == n - m:
        print(True)
    else:
        print(False)