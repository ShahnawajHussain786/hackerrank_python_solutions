# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:11:08 2023

@author: Shahnawaj Hussain
"""

def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 123)] 
    alphabet = alphabet[:size] 
    indexes = list(range(size)) 
    indexes = indexes[:-1]+indexes[::-1]

    for i in indexes:
        start_index = i+1
        original = alphabet[-start_index:]
        reverse = original[::-1]
        row = reverse + original[1:]
        row = '-'.join(row)
        width = size*4-3
        row = row.center(width, '-')
        print(row)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)