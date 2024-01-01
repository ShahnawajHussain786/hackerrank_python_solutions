# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:03:02 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
Country = set()
for i in range(n):
    Country.add(input())
print(len(Country))