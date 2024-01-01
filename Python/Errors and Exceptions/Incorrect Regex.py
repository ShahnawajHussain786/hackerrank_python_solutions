# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:49:00 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):  
    try:
        reg = input()
        re.compile(reg)
        print(True)
    except re.error:
        print(False)