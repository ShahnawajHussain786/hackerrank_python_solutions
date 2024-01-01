# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:39:03 2023

@author: Shahnawaj Hussain
"""

def swap_case(s):
    result = ""
    for i in s:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)