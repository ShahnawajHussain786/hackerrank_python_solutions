# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:41:04 2023

@author: Shahnawaj Hussain
"""

def split_and_join(line):
    # write your code here
    line = line.split(' ')
    line = '-'.join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)