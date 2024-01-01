# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:10:25 2024

@author: Shahnawaj Hussain
"""

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    t = len(node.attrib.keys())
    for child in node:
        if child:
            t += get_attr_number(child)
        else:
            t += len(child.attrib.keys())
    return t

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))