# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:06:35 2024

@author: Shahnawaj Hussain
"""


import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

new_matrix = []

for j in range(m):
    for row in matrix:
        new_matrix.append(row[j])

matrix = "".join(new_matrix)
matrix = re.sub(r"(?<=\w)([^\w]+)(?=\w)", r" ", matrix)
print(matrix)
    
    
