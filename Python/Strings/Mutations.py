# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:50:41 2023

@author: Shahnawaj Hussain
"""

def mutate_string(string, position, character):
    ls = list(string)
    ls[position] = character
    return "".join(ls)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)