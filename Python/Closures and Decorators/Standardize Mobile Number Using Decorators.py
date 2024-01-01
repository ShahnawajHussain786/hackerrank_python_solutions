# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:19:27 2024

@author: Shahnawaj Hussain
"""

def wrapper(f):
    def fun(l):
        f(map(lambda n: f'+91 {n[-10:-5]} {n[-5:]}', l))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
