# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:46:28 2023

@author: Shahnawaj Hussain
"""

def print_full_name(first, last):
    print('Hello'+' ' +first+ ' ' +last+'!'+' '+'You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)