# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:58:51 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
        s = input()
        result = "Valid" if len(re.findall(r'[A-Z]',s))>1 and len(re.findall(r'\d',s))>2 and len(set(re.findall(r'[a-zA-Z0-9]',s))) == 10 else "Invalid"
        print(result)