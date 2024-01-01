# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:09:54 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
l = input().split()
print(all(int(i) > 0 for i in l) and any(i == i[::-1] for i in l))
