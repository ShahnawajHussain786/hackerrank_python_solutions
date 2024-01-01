# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:52:48 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_attr(self, attrs):
        for attr_val_tuple in attrs:
            print("->", attr_val_tuple[0], ">", attr_val_tuple[1])

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attr(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attr(attrs)


parser = CustomHTMLParser()

n = int(input())

s = "".join(input() for i in range(n))
parser.feed(s)

"""
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
"""
