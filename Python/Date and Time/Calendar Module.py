# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:50:41 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())