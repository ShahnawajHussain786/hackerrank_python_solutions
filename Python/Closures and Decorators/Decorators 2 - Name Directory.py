# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:22:21 2024

@author: Shahnawaj Hussain
"""


def person_lister(f):
    def inner(people):
        return [f(p) for p in sorted(people, key=lambda x: (int(x[2])))]

    return inner



@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')