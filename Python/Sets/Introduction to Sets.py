# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:53:41 2023

@author: Shahnawaj Hussain
"""

def average(array):
    # your code goes here
    my_set = set(array)
    avg = sum(my_set)/len(my_set)
    
    return (avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)