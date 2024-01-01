# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:46:25 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)
