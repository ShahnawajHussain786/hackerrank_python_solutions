# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:42:24 2024

@author: Shahnawaj Hussain
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for c in range(int(input())):
    i = input().split()
    getattr(d, i[0])(int(i[1])) if len(i) > 1 else getattr(d, i[0])()
    
print(*d)
