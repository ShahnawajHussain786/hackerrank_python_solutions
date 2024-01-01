# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:55:16 2023

@author: Shahnawaj Hussain
"""

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if i.isalnum():
            alnum = alnum or i.isalnum()
        if i.isalpha():
            alpha = alpha or i.isalpha()
        if i.isdigit():
            digit = digit or i.isdigit()
        if i.islower():
            lower = lower or i.islower()
        if i.isupper():
            upper = upper or i.isupper()

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)


