# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:58:51 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
i = 0
t = []
for x in string:
    if x ==i:
        t[-1:][0][0]+=1       
    else:
        t.append([1,int(x)])
    i=x   
print(' '.join([str(tuple(x)) for x in t]))