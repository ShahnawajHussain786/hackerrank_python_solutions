# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:52:16 2023

@author: Shahnawaj Hussain
"""

def count_substring(string, sub_string):
    c = 0
    while sub_string in string:
        id = string.index(sub_string)
        c += 1
        string = string[id+1:]
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)