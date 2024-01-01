# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:49:31 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
n = int(input())
for i in range(n):
    s = input()
    parsed_email = email.utils.parseaddr(s)[1].strip()
    match_result = bool(
        re.match(
            r"(^[A-Za-z][A-Za-z0-9\._-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$", parsed_email
        )
    )
    if match_result:
        print(s)

        