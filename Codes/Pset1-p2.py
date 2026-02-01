# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 06:22:57 2026

@author: Boechat
"""

s='azcbobobegghakl'
times = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        times+=1
print('Number of times bob occurs is:',times)