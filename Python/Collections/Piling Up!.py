# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:48:17 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

case = int(input())
for i in range(case):
    n = int(input())
    dq = deque(map(int, input().split()))
    possible = True
    element = (2**31) + 1
    while dq:
        left_element = dq[0]
        right_element = dq[-1]
        if left_element >= right_element and element >= left_element:
            element = dq.popleft()
        elif right_element >= left_element and element >= right_element:
            element = dq.pop()
        else:
            possible = False
            break
    if possible:
        print("Yes")
    else:
        print("No")
