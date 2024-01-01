# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:28:16 2023

@author: Shahnawaj Hussain
"""

def is_leap(year):
    leap = False
    # Write your logic here
    if (year%4 ==0)and(year%100 != 0)or(year%400==0):
        
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))