# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:11:42 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
fields = input().split()
marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    marks += int(student.MARKS)
print((marks / n))
