# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:09:17 2023

@author: Shahnawaj Hussain
"""

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        de = str(i)
        oc = oct(i)[2:]
        he = hex(i)[2:].upper()
        bi = bin(i)[2:]
        print(de.rjust(width),oc.rjust(width),he.rjust(width),bi.rjust(width))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)