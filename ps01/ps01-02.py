# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 23:09:34 2017

@author: Rayon
"""

find_str = 'bob'
spos = 0
n = 0
for spos in range(len(s) - len(find_str) + 1):
    if s[spos:spos+len(find_str)] == find_str:
         n += 1
print (n)