# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:45:10 2024

@author: Shahnawaj Hussain
"""


import collections

if __name__ == '__main__':
    s = sorted(input().strip())
    s_counter = collections.Counter(s).most_common()
    s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
    for i in range(3):
        print(s_counter[i][0], s_counter[i][1])
    
