# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:06:01 2023

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
print('WELCOME'.center(m,'-'))
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))