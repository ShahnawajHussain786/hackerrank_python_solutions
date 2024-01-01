# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:36:04 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
r = re.search(r"([A-Za-z0-9])\1", s)
if r is None:
    print(-1)
else:
    print(r[1])