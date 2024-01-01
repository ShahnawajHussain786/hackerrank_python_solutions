# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:03:50 2023

@author: Shahnawaj Hussain
"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)