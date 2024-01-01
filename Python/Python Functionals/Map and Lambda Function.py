# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:16:09 2024

@author: Shahnawaj Hussain
"""

cube = lambda x:x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    a = [0, 1]
    if n < 2:
        return a[:n]
    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])
    return a

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))