# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:28:12 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import compile

pattern = compile("^[-+]?\d*\.\d+$")
for _ in range(int(input())):
    print(bool(pattern.match(input())))