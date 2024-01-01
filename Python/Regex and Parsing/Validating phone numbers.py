# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:47:53 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
[print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(int(input()))]
