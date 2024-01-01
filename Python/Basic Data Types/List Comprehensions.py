# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:32:22 2023

@author: Shahnawaj Hussain
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = []
    [l.append([i,j,k])for i in range(x+1)for j in range(y+1)for k in range(z+1)if (i+j+k )!=n]
    print(l)