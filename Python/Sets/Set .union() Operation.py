# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:06:37 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
shah = set(map(int,input().split()))
n = int(input())
nawaj = set(map(int,input().split()))

print(len(set(shah.union(nawaj)))) 
