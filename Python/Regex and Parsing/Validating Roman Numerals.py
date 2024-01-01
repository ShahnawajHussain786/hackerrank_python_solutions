# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:43:34 2024

@author: Shahnawaj Hussain
"""

regex_pattern = r"^(M{,3})(CM|CD|D?C{,3})(XC|XL|L?X{,3})(IX|IV|V?I{,3})$"	
# Do not delete 'r'.
import re
print(str(bool(re.match(regex_pattern, input()))))