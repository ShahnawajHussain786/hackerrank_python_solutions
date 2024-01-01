# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:39:41 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input().strip()
k = input().strip()
s_len = len(s)
flag = False
for i in range(s_len):
    match_result = re.match(k, s[i:])
    if match_result:
        start_index = i + match_result.start()
        end_index = i + match_result.end() - 1
        print((start_index, end_index))
        flag = True
if flag == False:
    print("(-1, -1)")
