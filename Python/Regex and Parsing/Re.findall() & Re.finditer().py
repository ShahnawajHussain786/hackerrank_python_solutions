# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:38:04 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
result = re.findall(
    r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",
    s,
)
if result:
    for i in result:
        print(i)
else:
    print(-1)
