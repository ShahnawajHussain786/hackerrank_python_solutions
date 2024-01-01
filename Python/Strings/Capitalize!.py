# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:17:45 2023

@author: Shahnawaj Hussain
"""
import os
# Complete the solve function below.
def solve(s):
    result = ''
    for i in s.split(' '):
        result += i.capitalize() + ' '
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
