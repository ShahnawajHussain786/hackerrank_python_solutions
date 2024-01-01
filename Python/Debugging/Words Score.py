# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:25:13 2024

@author: Shahnawaj Hussain
"""

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum(1 for letter in word if is_vowel(letter))
        score += 2 if num_vowels % 2 == 0 else 1
    return score