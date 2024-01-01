# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:07:55 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
a = int(input())
b = Counter(map(int, input().split()))
c = int(input())

t_money = 0
for i in range(c):
    size, cost = map(int, input().split())
    if b[size]: 
        b[size] -= 1
        t_money += cost
print(t_money)
