# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:23:27 2023

@author: Shahnawaj Hussain
"""

def minion_game(string):
    # your code goes here
    '''Calculates name of Winner and their score'''
    stuart = 0
    kevin = 0
    l = len(string)

    for i in range(l):
        for vowc in "AEIOU":
            if string[i].find(vowc) >= 0:
                kevin = kevin + l - i

    stuart = int(l*(l+1)/2) - kevin

    if stuart > kevin:
        print("Stuart " + str(stuart))
    if kevin > stuart:
        print("Kevin " + str(kevin))
    if kevin == stuart:
        print("Draw")

    return 0

if __name__ == '__main__':
    s = input()
    minion_game(s)