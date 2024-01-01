# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:38:10 2023

@author: Shahnawaj Hussain
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = len(scores)
student = sum(student_marks[query_name]) / l

        
print(format(student, '.2f'))
