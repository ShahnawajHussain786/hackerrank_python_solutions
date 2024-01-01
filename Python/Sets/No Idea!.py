# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:56:18 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    A = set(map(int, input().strip().split(' ')))
    B = set(map(int, input().strip().split(' ')))
    
    for i in arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)
