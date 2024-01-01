# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:57:04 2024

@author: Shahnawaj Hussain
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs)

    def handle_attrs(self, attrs):
        for attrs_pair in attrs:
            print("->", attrs_pair[0].strip(), ">", attrs_pair[1].strip())

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
