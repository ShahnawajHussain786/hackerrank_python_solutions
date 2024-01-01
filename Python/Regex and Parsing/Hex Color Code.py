# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:51:10 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for j in range(n):
    s = input()
    result = re.findall(r"(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})", s)
    for i in result:
        if i != "":
            print(i)