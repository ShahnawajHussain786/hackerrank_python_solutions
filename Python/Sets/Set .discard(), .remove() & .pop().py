# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:04:32 2023

@author: Shahnawaj Hussain
"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        try:
            s.remove(int(cmd[1]))
        except:
            continue
    elif cmd[0] == "discard":
        try:
            s.discard(int(cmd[1]))
        except:
            continue
print(sum(s))
 
