# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:07:49 2024

@author: Shahnawaj Hussain
"""




if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for i in sorted(arr, key=lambda x: x[k]):
        print(*i)
