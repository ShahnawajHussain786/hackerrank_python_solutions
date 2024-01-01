# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:39:46 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
elements = int(input())
i_set = set(map(int, input().split()))
no_sets = int(input())
for _ in range(no_sets):
    cmd = input().split()
    opt = cmd[0]
    other_set = set(map(int, input().split()))
    if opt == "difference_update":
        i_set.difference_update(other_set)
    elif opt == "intersection_update":
        i_set.intersection_update(other_set)
    elif opt == "symmetric_difference_update":
        i_set.symmetric_difference_update(other_set)
    elif opt == "update":
        i_set.update(other_set)
print(sum(i_set))
