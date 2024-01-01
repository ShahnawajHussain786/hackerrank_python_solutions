# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:36:08 2023

@author: Shahnawaj Hussain
"""

if __name__ == '__main__':
    n = int(input())
    m = map(int, input().split())
    tup = ()
    for x in m:
        tup+=(x,)
    print(hash(tup))