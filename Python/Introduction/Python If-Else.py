# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 12:59:57 2023

@author: Shahnawaj Hussain
"""

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 !=0:
        print("Weird")
    elif 2<= n <=5:
        print("Not Weird")
    elif n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
