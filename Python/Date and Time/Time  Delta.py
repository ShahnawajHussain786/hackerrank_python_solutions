# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:52:22 2024

@author: Shahnawaj Hussain
"""


import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_date = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2_date = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    if t1_date > t2_date:
        time_diff = t1_date - t2_date
    else:
        time_diff = t2_date - t1_date
    if time_diff.days == 0:
        time_diff_seconds = time_diff.seconds
    else:
        time_diff_seconds = time_diff.days * 24 *3600 + time_diff.seconds
    return str(time_diff_seconds)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
