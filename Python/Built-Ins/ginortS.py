# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:11:28 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
print(
    "".join(
        sorted(
            s,
            key=lambda x: (
                x.isdigit() and int(x) % 2 == 0,
                x.isdigit(),
                x.isupper(),
                x.islower(),
                x,
                ),
            )
        )
    )
