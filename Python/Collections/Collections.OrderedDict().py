# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:13:30 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
a = OrderedDict()
n = int(input())
for _ in range(n):
    item_name, space, net_price = input().rpartition(' ')
    a[item_name] = a.get(item_name, 0) + int(net_price)
for item_name, net_price in a.items():
    print(item_name, net_price)
