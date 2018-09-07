# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:47:46 2018

@author: mihalev
"""

s =input()
ind = 1
count = 0
f = 'bob'
while ind != -1:
    ind = s.find(f)
    if ind >= 0:
        count += 1
    s = s[ind+1:]
print(count)